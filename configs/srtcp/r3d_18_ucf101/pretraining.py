_base_ = '../pretraining_runtime_ucf.py'

work_dir = './output/srtcp/r3d_18_ucf101/pretraining/'

model = dict(
    type='SRTCP',
    backbone=dict(
        type='R3D',
        depth=18,
        num_stages=4,
        stem=dict(
            temporal_kernel_size=3,
            temporal_stride=1,
            in_channels=3,
            with_pool=False,
        ),
        down_sampling=[False, True, True, False],
        down_sampling_temporal=[False, True, True, True],
        channel_multiplier=1.0,
        bottleneck_multiplier=1.0,
        with_bn=True,
        zero_init_residual=False
    ),
    head=dict(
        in_channels=512,
        in_temporal_size=2,
        hidden_channels=512,
        roi_feat_size=5,
        spatial_stride=8,
        num_pred_frames=16,
        target_means=(0., 0., 0., 0.),
        target_stds=(0.8, 0.8, 0.04, 0.04),
    ),
    in_channels=512,
    out_channels=128,
    queue_size=8192,
    mlp=True,
    temperature=0.2,
)


