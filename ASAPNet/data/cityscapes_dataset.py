"""
Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).
"""

import os.path
from data.pix2pix_dataset import Pix2pixDataset
from data.image_folder import make_dataset

class CityscapesDataset(Pix2pixDataset):

    @staticmethod
    def modify_commandline_options(parser, is_train):
        parser = Pix2pixDataset.modify_commandline_options(parser, is_train)
        parser.set_defaults(preprocess_mode='fixed')
        parser.set_defaults(load_size=1024)
        parser.set_defaults(crop_size=1024)
        parser.set_defaults(display_winsize=512)
        parser.set_defaults(label_nc=35)
        parser.set_defaults(aspect_ratio=2.0)
        parser.set_defaults(batchSize=2)
        parser.set_defaults(lr_instance=True)
        parser.set_defaults(no_instance_dist=True)
        parser.set_defaults(no_instance_edge=False)

        opt, _ = parser.parse_known_args()
        if hasattr(opt, 'num_upsampling_layers'):
            parser.set_defaults(num_upsampling_layers='more')
        if opt.center_crop:
            parser.set_defaults(crop_size=256)
            parser.set_defaults(display_winsize=256)
            parser.set_defaults(preprocess_mode='scale_width_and_crop')
        return parser

    def get_paths(self, opt):
        root = opt.dataroot
        phase = 'test' if opt.phase == 'test' else 'train'

        #label_dir = os.path.join(root, 'gtFine', phase)
        label_dir = os.path.join(root, '%s_label'%phase)
        label_paths_all = make_dataset(label_dir, recursive=True)
        label_paths = [p for p in label_paths_all]
        # label_paths = [p for p in label_paths_all if p.endswith('_labelIds.png')]
        print('label_paths', len(label_paths))

        #image_dir = os.path.join(root, 'leftImg8bit', phase)
        image_dir = os.path.join(root, '%s_img'%phase)
        image_paths = make_dataset(image_dir, recursive=True)

        if not (opt.no_instance_edge & opt.no_instance_dist):
            instance_dir = os.path.join(root, '%s_inst'%phase)
            instance_paths_all = make_dataset(instance_dir, recursive=True)
            instance_paths = [p for p in instance_paths_all]
            # instance_paths = [p for p in label_paths_all if p.endswith('_instanceIds.png')]
        else:
            instance_paths = []
        
        print('instance_paths', len(instance_paths), opt.no_instance_edge, opt.no_instance_dist)
        print('image_paths', len(image_paths))

        return label_paths, image_paths, instance_paths

    def paths_match(self, path1, path2):
        name1 = os.path.basename(path1)
        name2 = os.path.basename(path2)
        # compare the first 3 components, [city]_[id1]_[id2]
        return '_'.join(name1.split('_')[:3]) == \
            '_'.join(name2.split('_')[:3])
