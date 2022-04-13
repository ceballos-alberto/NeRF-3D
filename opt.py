# Training options  - NeRF3D Alteia #
# Author >> Alberto Ceballos

# Import reauired libraries #
import argparse

def get_opts():

    parser = argparse.ArgumentParser()

    # Root directory of dataset #
    parser.add_argument('--root_dir',
                        type=str,
                        default='/home/alberto/data/demo',
                        help='root directory of dataset')

    # Type of dataset #
    parser.add_argument('--dataset_name',
                        type=str,
                        default='blender',
                        choices=['blender', 'llff'],
                        help='which dataset to train/val')

    # Resolution of the input images #
    parser.add_argument('--img_wh',
                        nargs="+",
                        type=int,
                        default=[800, 800],
                        help='resolution (img_w, img_h) of the image')

    # 360 inward-facing images for 3D reconstruction #
    parser.add_argument('--spheric_poses',
                        default=False,
                        action="store_true",
                        help='whether images are taken in spheric poses (for llff)')

    # Number of frequencies in xyz positional encoding #
    parser.add_argument('--N_emb_xyz',
                        type=int,
                        default=10,
                        help='number of frequencies in xyz positional encoding')

    # Number of frequencies in dir positional encoding #
    parser.add_argument('--N_emb_dir',
                        type=int,
                        default=4,
                        help='number of frequencies in dir positional encoding')

    # Number of coarse samples #
    parser.add_argument('--N_samples',
                        type=int,
                        default=64,
                        help='number of coarse samples')

    # Number of additional fine samples #
    parser.add_argument('--N_importance',
                        type=int,
                        default=128,
                        help='number of additional fine samples')

    # Use disparity depth sampling #
    parser.add_argument('--use_disp',
                        default=False,
                        action="store_true",
                        help='use disparity depth sampling')

    # Factor to perturb depth sampling points #
    parser.add_argument('--perturb',
                        type=float,
                        default=1.0,
                        help='factor to perturb depth sampling points')

    # Std dev of noise added to regularize sigma #
    parser.add_argument('--noise_std',
                        type=float,
                        default=1.0,
                        help='std dev of noise added to regularize sigma')

    # Batch size #
    parser.add_argument('--batch_size',
                        type=int,
                        default=1024,
                        help='batch size')

    # Chunk size - number of rays processed at the same time #
    parser.add_argument('--chunk',
                        type=int,
                        default=32*1024,
                        help='chunk size to split the input to avoid OOM')

    # Number of epochs #
    parser.add_argument('--num_epochs',
                        type=int,
                        default=16,
                        help='number of training epochs')

    # Number of GPUs #
    parser.add_argument('--num_gpus',
                        type=int,
                        default=2,
                        help='number of gpus')

    # Pretrained checkpoint to load #
    parser.add_argument('--ckpt_path',
                        type=str,
                        default=None,
                        help='pretrained checkpoint to load (including optimizers, etc)')

    # Prefixes to ignore in the checkpoint #
    parser.add_argument('--prefixes_to_ignore',
                        nargs='+',
                        type=str,
                        default=['loss'],
                        help='the prefixes to ignore in the checkpoint state dict')

    # Pretrained model weights to load #
    parser.add_argument('--weight_path',
                        type=str,
                        default=None,
                        help='pretrained model weight to load (do not load optimizers, etc)')

    # Optimizer #
    parser.add_argument('--optimizer',
                        type=str,
                        default='adam',
                        help='optimizer type',
                        choices=['sgd', 'adam', 'radam', 'ranger'])

    # Learning rate #
    parser.add_argument('--lr',
                        type=float,
                        default=5e-4,
                        help='learning rate')

    # Momentum of the learning rate #
    parser.add_argument('--momentum',
                        type=float,
                        default=0.9,
                        help='learning rate momentum')

    # Weight decay #
    parser.add_argument('--weight_decay',
                        type=float,
                        default=0,
                        help='weight decay')

    # Scheduler type #
    parser.add_argument('--lr_scheduler',
                        type=str,
                        default='steplr',
                        help='scheduler type',
                        choices=['steplr', 'cosine', 'poly'])

    # Warmup multiplier (sgd or adam only) #
    parser.add_argument('--warmup_multiplier',
                        type=float,
                        default=1.0,
                        help='lr is multiplied by this factor after --warmup_epochs)

    # Warmup epochs (sgd or adam only) #
    parser.add_argument('--warmup_epochs',
                        type=int,
                        default=0,
                        help='Gradually warm-up(increasing) learning rate in optimizer')

    # Scheduler decay step (steplr only) #
    parser.add_argument('--decay_step',
                        nargs='+',
                        type=int,
                        default=[20],
                        help='scheduler decay step')

    # learning rate decay amount (steplr only)#
    parser.add_argument('--decay_gamma',
                        type=float,
                        default=0.1,
                        help='learning rate decay amount')

    # Exponent for polynomial learning rate decay (poly only) #
    parser.add_argument('--poly_exp',
                        type=float,
                        default=0.9,
                        help='exponent for polynomial learning rate decay')

    # Experiment name #
    parser.add_argument('--exp_name',
                        type=str,
                        default='exp',
                        help='experiment name')

    return parser.parse_args()

# This is the end of the code #
