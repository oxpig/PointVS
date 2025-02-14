"""Set up rather large command line argument list"""

import argparse


def parse_args():  #pylint:disable=too-many-statements
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('model', type=str,
                        help='Type of point cloud network to use: '
                             'lucid or egnn')
    parser.add_argument('--train_data_root_pose', type=str,
                        help='Location relative to which parquets files for '
                             'training the pose classifier as specified in the '
                             'train_types_pose file are stored.')
    parser.add_argument('--train_data_root_affinity', '--tdra', type=str,
                        help='Location relative to which parquets files for '
                             'training the affinity predictor as specified in '
                             'the train_types file are stored.')
    parser.add_argument('--test_data_root_pose', type=str,
                        help='Location relative to which parquets files for '
                             'testing the pose classifier as specified in the '
                             'test_types_pose file are stored.')
    parser.add_argument('--test_data_root_affinity', type=str,
                        help='Location relative to which parquets files for '
                             'testing the affinity predictor as specified in '
                             'the test_types file are stored.')
    parser.add_argument('save_path', type=str,
                        help='Directory in which experiment outputs are '
                             'stored. If wandb_run and wandb_project are '
                             'specified, save_path/wandb_project/wandb_run '
                             'will be used to store results.')
    parser.add_argument('--logging_level', type=str, default='info',
                        help='Level at which to print logging statements. Any '
                        'of notset, debug, info, warning, error, critical.')
    parser.add_argument('--load_weights', '-l', type=str, required=False,
                        help='Load a model.')
    parser.add_argument('--translated_actives', type=str,
                        help='Directory in which translated actives are stored.'
                             ' If unspecified, no translated actives will be '
                             'used. The use of translated actives are is '
                             'discussed in https://pubs.acs.org/doi/10.1021/ac'
                             's.jcim.0c00263')
    parser.add_argument('--batch_size', '-b', type=int, required=False,
                        default=32,
                        help='Number of examples to include in each batch for '
                             'training.')
    parser.add_argument('--epochs_pose', '-ep', type=int, required=False,
                        default=0,
                        help='Number of times to iterate through pose '
                             'training set.')
    parser.add_argument('--epochs_affinity', '-ea', type=int, required=False,
                        default=0,
                        help='Number of times to iterate through affinity '
                             'training set.')
    parser.add_argument('--channels', '-k', type=int, default=32,
                        help='Channels for feature vectors')
    parser.add_argument('--learning_rate', '-lr', type=float, default=0.002,
                        help='Learning rate for gradient descent')
    parser.add_argument('--weight_decay', '-w', type=float, default=1e-4,
                        help='Weight decay for regularisation')
    parser.add_argument('--wandb_project', type=str,
                        help='Name of wandb project. If left blank, wandb '
                             'logging will not be used.')
    parser.add_argument('--wandb_run', type=str,
                        help='Name of run for wandb logging.')
    parser.add_argument('--layers', type=int, default=6,
                        help='Number of layers in LieResNet')
    parser.add_argument('--radius', type=int, default=10,
                        help='Maximum distance from a ligand atom for a '
                             'receptor atom to be included in input')
    parser.add_argument('--load_args', type=str,
                        help='Load yaml file with command line args. Any args '
                             'specified in the file will overwrite other args '
                             'specified on the command line.')
    parser.add_argument('--double', action='store_true',
                        help='Use 64-bit floating point precision')
    parser.add_argument('--activation', type=str, default='relu',
                        help='Activation function')
    parser.add_argument('--dropout', type=float, default=0.0,
                        help='Chance for nodes to be inactivated on each '
                             'trainin batch (EGNN)')
    parser.add_argument('--use_1cycle', action='store_true',
                        help='Use 1cycle learning rate scheduling')
    parser.add_argument('--warm_restarts', action='store_true',
                        help='Use cosine annealing with warm restarts')
    parser.add_argument('--fourier_features', type=int, default=0,
                        help='(Lucid) Number of fourier terms to use when '
                             'encoding distances (default is not to use '
                             'fourier distance encoding)')
    parser.add_argument('--norm_coords', action='store_true',
                        help='(Lucid) Normalise coordinate vectors')
    parser.add_argument('--norm_feats', action='store_true',
                        help='(Lucid) Normalise feature vectors')
    parser.add_argument('--use_atomic_numbers', action='store_true',
                        help='Use atomic numbers rather than smina types')
    parser.add_argument('--compact', action='store_true',
                        help='Use compact rather than true one-hot encodings')
    parser.add_argument('--thin_mlps', action='store_true',
                        help='(Lucid) Use single layer MLPs for edge, node and '
                             'coord updates')
    parser.add_argument('--hydrogens', action='store_true',
                        help='Include polar hydrogens')
    parser.add_argument('--augmented_actives', type=int, default=0,
                        help='Number of randomly rotated actives to be '
                             'included as decoys during training')
    parser.add_argument('--min_aug_angle', type=float, default=30,
                        help='Minimum angle of rotation for augmented actives '
                             'as specified in the augmented_actives argument')
    parser.add_argument('--max_active_rmsd', type=float,
                        help='(Pose selection) maximum non-aligned RMSD '
                             'between the original crystal pose and active '
                             'redocked poses')
    parser.add_argument('--min_inactive_rmsd', type=float,
                        help='(Pose selection) minimum non-aligned RMSD '
                             'between original crystal pose and inactive '
                             'redocked poses')
    parser.add_argument('--val_on_epoch_end', '-v', action='store_true',
                        help='Run inference ion the validation set at the end '
                             'of every epoch during training')
    parser.add_argument('--synth_pharm', '-p', action='store_true',
                        help='Synthetic Pharmacophore mode (for Tom, beta)')
    parser.add_argument('--input_suffix', '-s', type=str, default='parquet',
                        help='Filename extension for inputs')
    parser.add_argument('--train_types_pose', type=str,
                        help='Optional name of GNINA-like types file which '
                             'contains paths and labels for a pose training '
                             'set. '
                             'See GNINA 1.0 documentation for specification.')
    parser.add_argument('--train_types_affinity', type=str,
                        help='Optional name of GNINA-like types file which '
                             'contains paths and labels for an affinity '
                             'training set. '
                             'See GNINA 1.0 documentation for specification.')
    parser.add_argument('--test_types_pose', type=str,
                        help='Optional name of GNINA-like types file which '
                             'contains paths and labels for a pose test set. '
                             'See GNINA 1.0 documentation for specification.')
    parser.add_argument('--test_types_affinity', type=str,
                        help='Optional name of GNINA-like types file which '
                             'contains paths and labels for an affinity test set. '
                             'See GNINA 1.0 documentation for specification.')
    parser.add_argument('--egnn_attention', action='store_true',
                        help='Use attention mechanism on edges for EGNN')
    parser.add_argument('--egnn_tanh', action='store_true',
                        help='Put tanh layer at the end of the coordinates '
                             'mlp (EGNN)')
    parser.add_argument('--egnn_normalise', action='store_true',
                        help='Normalise radial coordinates (EGNN)')
    parser.add_argument('--egnn_residual', action='store_true',
                        help='Use residual connections (EGNN)')
    parser.add_argument('--edge_radius', type=float, default=4.0,
                        help='Maximum interatomic distance for an edge to '
                             'exist (EGNN)')
    parser.add_argument('--end_flag', action='store_true',
                        help='Add a file named "_FINISHED" to the save_path '
                             'upon training and test completion')
    parser.add_argument('--wandb_dir', type=str,
                        help='Location to store wandb files. Defaults to '
                             '<save_path>/<wandb_project>/<wandb_run>/wandb.')
    parser.add_argument('--estimate_bonds', action='store_true',
                        help='(EGNN): Instead of using a fixed edge radius,'
                             'the intermolecular radius is set at '
                             '--edge_radius Angstroms but the intramolecular '
                             'radius is set at 2A, which has the effect of '
                             'putting edges where there are covalent bonds '
                             'between atoms in the same molecule.')
    parser.add_argument('--linear_gap', action='store_true',
                        help='Final linear layer comes after rather than '
                             'before the global average pooling layer. This '
                             'can improve performance significantly.')
    parser.add_argument('--prune', action='store_true',
                        help='(EGNN) Prune subgraphs which are not connected '
                             'to the ligand')
    parser.add_argument('--top1', action='store_true',
                        help='A poorly kept secret ;)')
    parser.add_argument('--graphnorm', action='store_true',
                        help='(EGNN) add GraphNorm layers to each node MLP')
    parser.add_argument('--multi_fc', action='store_true',
                        help='Three fully connected layers rather than just '
                             'one to summarise the graph at the end of '
                             'the EGNN')
    parser.add_argument('--lucid_node_final_act', action='store_true',
                        help='(Lucid) SiLU at the end of node MLPs')
    parser.add_argument('--p_remove_entity', type=float, default=0,
                        help='Rate at which one of (randomly selected) ligand '
                             'or receptor is removed and label is forced to '
                             'zero')
    parser.add_argument('--static_coords', action='store_true',
                        help='Do not update coords (eq. 4, EGNN)')
    parser.add_argument('--permutation_invariance', action='store_true',
                        help='Edge features are invariant to order of input '
                             'node (EGNN, experimental)')
    parser.add_argument('--node_attention', action='store_true',
                        help='Use attention mechanism for nodes')
    parser.add_argument('--attention_activation_function', type=str,
                        default='sigmoid', help='One of sigmoid, relu, silu '
                                                'or tanh')
    parser.add_argument('--node_attention_final_only', action='store_true',
                        help='Only apply attention mechanism to nodes in the '
                             'final layer')
    parser.add_argument('--edge_attention_final_only', action='store_true',
                        help='Only apply attention mechanism to edges in the '
                             'final layer')
    parser.add_argument('--node_attention_first_only', action='store_true',
                        help='Only apply attention mechanism to nodes in the '
                             'first layer')
    parser.add_argument('--edge_attention_first_only', action='store_true',
                        help='Only apply attention mechanism to edges in the '
                             'first layer')
    parser.add_argument('--only_save_best_models', action='store_true',
                        help='Only save models which improve upon previous '
                             'models')
    parser.add_argument('--egnn_edge_residual', action='store_true',
                        help='Residual connections for individual messages '
                             '(EGNN)')
    parser.add_argument('--gated_residual', action='store_true',
                        help='Residual connections are gated by a single '
                             'learnable parameter (EGNN), see '
                             'home.ttic.edu/~savarese/savarese_files/Residual_Gates.pdf')
    parser.add_argument('--rezero', action='store_true',
                        help='ReZero residual connections (EGNN), see '
                             'arxiv.org/pdf/2003.04887.pdf')
    parser.add_argument('--extended_atom_types', action='store_true',
                        help='18 atom types rather than 10')
    parser.add_argument('--max_inactive_rmsd', type=float,
                        help='Discard structures beyond <x> RMSD from xtal '
                             'pose')
    parser.add_argument('--model_task', type=str, default='classification',
                        help='One of either classification or regression; ')
    parser.add_argument('--synthpharm', action='store_true', help='For tom')
    parser.add_argument('--p_noise', type=float, default=-1,
                        help='Probability of label being inverted during '
                             'training')
    parser.add_argument('--include_strain_info', action='store_true',
                        help='Include info on strain energy and RMSD from '
                             'ground state of ligand')
    parser.add_argument('--final_softplus', action='store_true',
                        help='Final layer in regression has softplus '
                             'nonlinearity')
    parser.add_argument('--optimiser', '-o', type=str, default='adam',
                        help='Optimiser (either adam or sgd)')
    parser.add_argument('--multi_target_affinity', action='store_true',
                        help='Use multitarget regression for affinity. If '
                             'True, targets are split depending on if labels '
                             'are pkd, pki or IC50.')
    parser.add_argument('--regression_loss', type=str, default='mse',
                        help='Either mse or huber.')
    return parser.parse_args()
