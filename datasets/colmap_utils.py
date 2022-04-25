import os
import sys
import collections
import numpy as np
import struct

# Data structures for cameras, images and 3D points #

CameraModel = collections.namedtuple(
    "CameraModel", ["model_id", "model_name", "num_params"])

Camera = collections.namedtuple("Camera", ["id", "origin", "model", "width",
"height", "params"])

Image = collections.namedtuple("Image", ["id", "origin", "origin_cam", "qvec",
"tvec", "camera_id", "name", "xys", "point3D_ids"])

Point3D = collections.namedtuple(
    "Point3D", ["id", "xyz", "rgb", "error", "image_ids", "point2D_idxs"])




CAMERA_MODELS = {
    CameraModel(model_id=0, model_name="SIMPLE_PINHOLE", num_params=3),
    CameraModel(model_id=1, model_name="PINHOLE", num_params=4),
    CameraModel(model_id=2, model_name="SIMPLE_RADIAL", num_params=4),
    CameraModel(model_id=3, model_name="RADIAL", num_params=5),
    CameraModel(model_id=4, model_name="OPENCV", num_params=8),
    CameraModel(model_id=5, model_name="OPENCV_FISHEYE", num_params=8),
    CameraModel(model_id=6, model_name="FULL_OPENCV", num_params=12),
    CameraModel(model_id=7, model_name="FOV", num_params=5),
    CameraModel(model_id=8, model_name="SIMPLE_RADIAL_FISHEYE", num_params=4),
    CameraModel(model_id=9, model_name="RADIAL_FISHEYE", num_params=5),
    CameraModel(model_id=10, model_name="THIN_PRISM_FISHEYE", num_params=12)
}
CAMERA_MODEL_IDS = dict([(camera_model.model_id, camera_model) \
                         for camera_model in CAMERA_MODELS])


def read_next_bytes (fid, num_bytes, format_char_sequence, endian_character="<"):
    data = fid.read(num_bytes)
    return struct.unpack(endian_character + format_char_sequence, data)

def change_name(selected, real):
    for index, element in enumerate(real):
        real[index] = selected.index(element)
    return real

""" ----------------------------------------------------------------------------
    Function name : Read Cameras.
    Description : Save information of the cameras in a dictionary.
    Revised : 25/04/22.
---------------------------------------------------------------------------- """

def read_cameras(path, selected, info=False):

    # Dictionary to store the cameras #
    cameras = {}

    # Open the file #
    with open(path, "rb") as file:

        # Number of cameras in the file #
        num_cameras = read_next_bytes(file, 8, "Q")[0]

        # Read camera by camera #
        for line in range(num_cameras):

            camera_properties = read_next_bytes(file, 24, "iiQQ")
            camera_id = camera_properties[0]
            origin = camera_id
            model_id = camera_properties[1]
            width = camera_properties[2]
            height = camera_properties[3]
            model_name = CAMERA_MODEL_IDS[model_id].model_name
            num_params = CAMERA_MODEL_IDS[model_id].num_params
            params = read_next_bytes(file, 8*num_params, "d"*num_params)

            # Save info only when the camera is used #
            if camera_id in selected:

                # Change the camera ID and save info #
                camera_id = selected.index(camera_id)

                # Save data in the dictionary #
                cameras[camera_id] = Camera(id=camera_id, origin=origin,
                model=model_name, width=width, height=height, params=np.array(params))

    # Display information #
    if (info==True):
        print(" ")
        print("===============================================================")
        print("     Information about the cameras")
        print("===============================================================")
        print(" ")
        print(" - Number of cameras >> {}".format(len(cameras)))
        print(" ")
        for cam in cameras.values():
            print("========== Camera ID >> {}".format(cam.id))
            print(" ")
            print(" - Original Camera ID >> {}".format(cam.origin))
            print(" - Model >> {}".format(cam.model))
            print(" - Width >> {}".format(cam.width))
            print(" - Height >> {}".format(cam.height))
            print(" - parameters >> {}".format(cam.params))
            print(" ")

    # Return data #
    return cameras

""" ----------------------------------------------------------------------------
    Function name : Read Images.
    Description : Save information of the images in a dictionary.
    Revised : 25/04/22.
---------------------------------------------------------------------------- """

def read_images(path, selected, info=False):

    # Dictionary to store the images #
    images = {}

    # List of used cameras #
    camera_list = []

    # Open the file #
    with open(path, "rb") as file:

        # Number of images in the file #
        num_reg_images = read_next_bytes(file, 8, "Q")[0]

        # Read image by image #
        for image_index in range(num_reg_images):

            binary_image_properties = read_next_bytes(file, 64, "idddddddi")
            image_id = binary_image_properties[0]
            origin = image_id
            qvec = np.array(binary_image_properties[1:5])
            tvec = np.array(binary_image_properties[5:8])
            camera_id = binary_image_properties[8]
            origin_cam = camera_id
            image_name = ""
            current_char = read_next_bytes(file, 1, "c")[0]
            while current_char != b"\x00":
                image_name += current_char.decode("utf-8")
                current_char = read_next_bytes(file, 1, "c")[0]
            num_points2D = read_next_bytes(file, 8, "Q")[0]
            x_y_id_s = read_next_bytes(file, 24*num_points2D, "ddq"*num_points2D)
            xys = np.column_stack([tuple(map(float, x_y_id_s[0::3])),
            tuple(map(float, x_y_id_s[1::3]))])
            point3D_ids = np.array(tuple(map(int, x_y_id_s[2::3])))

            # Save info only when the camera is used #
            if image_id in selected:

                # Add camera to the list of used cameras #
                camera_list.append(camera_id)

                # Change the camera and image IDs #
                image_id = selected.index(image_id)
                camera_id = camera_list.index(camera_id)

                # Save data in the dictionary #
                images[image_id] = Image(id=image_id, origin=origin, origin_cam=origin_cam,
                qvec=qvec, tvec=tvec, camera_id=camera_id, name=image_name,
                xys=xys, point3D_ids=point3D_ids)

    # Display information #
    if (info==True):
        print(" ")
        print("===============================================================")
        print("     Information about the images")
        print("===============================================================")
        print(" ")
        print(" - Number of images >> {}".format(len(images)))
        print(" ")
        for img in images.values():
            print("========== Image ID >> {}".format(img.id))
            print(" ")
            print(" - Original Image ID >> {}".format(img.origin))
            print(" - Camera ID >> {}".format(img.camera_id))
            print(" - Original Camera ID >> {}".format(img.origin_cam))
            print(" - Image name >> {}".format(img.name))
            print(" - Qvec >> {}".format(img.qvec))
            print(" - Tvec >> {}".format(img.tvec))
            print(" - xys >> {}".format(img.xys))
            print(" - Points 3D >> {}".format(img.point3D_ids))
            print(" ")

    # Return data #
    return images, camera_list

""" ----------------------------------------------------------------------------
    Function name : Read Points.
    Description : Save information of the 3D points in a dictionary.
---------------------------------------------------------------------------- """

def read_points(path, selected):

    # Dictionary to store the 3D points #
    points3D = {}

    # Open the file #
    with open(path, "rb") as file:

        # Number of points in the file #
        num_points = read_next_bytes(file, 8, "Q")[0]

        # Read point by point #
        for line in range(num_points):

            binary_point_line_properties = read_next_bytes(file, 43, "QdddBBBd")
            point3D_id = binary_point_line_properties[0]
            xyz = np.array(binary_point_line_properties[1:4])
            rgb = np.array(binary_point_line_properties[4:7])
            error = np.array(binary_point_line_properties[7])
            track_length = read_next_bytes(file, 8, "Q")[0]
            track_elems = read_next_bytes(file, 8*track_length, "ii"*track_length)
            image_ids = np.array(tuple(map(int, track_elems[0::2])))
            point2D_idxs = np.array(tuple(map(int, track_elems[1::2])))

            # Transform image and point IDs #
            image_ids_list = image_ids.tolist()
            point2D_idxs_list = point2D_idxs.tolist()
            for index, element in enumerate(image_ids_list):
                if element not in selected:
                    image_ids_list[index] = -1
                    point2D_idxs_list[index] = -1
            try:
                while True:
                    image_ids_list.remove(-1)
            except ValueError:
                    pass
            try:
                while True:
                    point2D_idxs_list.remove(-1)
            except ValueError:
                    pass
            image_ids_list = change_name(selected, image_ids_list)
            image_ids = np.array(image_ids_list)
            point2D_idxs = np.array(point2D_idxs_list)

            # Save info only when the 3D point is used #
            if len(image_ids_list)>0:
                points3D[point3D_id] = Point3D(id=point3D_id, xyz=xyz, rgb=rgb,
                error=error, image_ids=image_ids, point2D_idxs=point2D_idxs)

    return points3D
