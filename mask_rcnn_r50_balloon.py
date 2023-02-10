_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_2x.py', '../_base_/default_runtime.py'
]

model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=1
            ),
        
        mask_head=dict(
            num_classes=1
            ))
)

data = dict(
    # 根据实验环境调整每个 batch_size 和 workers 数量
    samples_per_gpu = 8,
    workers_per_gpu = 2,
    # 指定训练集路径
    train = dict(
        img_prefix = 'data/balloon_dataset/train',
        ann_file = 'data/balloon_dataset/train.json',
        classes = ('balloon',)
    ),
    # 指定验证集路径
    val = dict(
        img_prefix = 'data/balloon_dataset/val',
        ann_file = 'data/balloon_dataset/val.json',
        classes = ('balloon',)
    )
)

# 优化器
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
#optimizer_config = dict(grad_clip=None)

# 学习率策略
lr_config = None

log_config = dict(
    interval=25,
    hooks=[
        dict(type='TextLoggerHook'),
    ])

runner = dict(type='EpochBasedRunner', max_epochs=20)

# 预训练模型
load_from = '/HOME/scz0apw/run/mmdetection/checkpoints/mask_rcnn_r50_fpn_2x_coco_bbox_mAP-0.392__segm_mAP-0.354_20200505_003907-3e542a40.pth'