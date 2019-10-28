import os

#data config
input_dir = '/media/gtmeng/DataDisk2/Learning-to-See-in-the-Dark-pre-processed/VBM4D_rawRGB'
gt_dir = '/media/gtmeng/DataDisk2/Learning-to-See-in-the-Dark-pre-processed/long'
train_crop_size=256


#train config
seed=0
train_batch_size=8
data_loader_num_workers=4
base_lr=1e-4
momentum=0.9
total_epochs=2000
lr_decay_epochs=[500,1000,1500]
lr_decay_rate=0.1
model_save_interval=50
model_save_path='./snapshots'
vgg_output_layer_list=[3,8,17,26]

if not os.path.exists(model_save_path):
    os.mkdir(model_save_path)

log_interval=4

start_epoch=1
for epoch in lr_decay_epochs:
    if epoch<=start_epoch:
        base_lr*=lr_decay_rate

if start_epoch>1:
    snapshot_path=os.path.join(model_save_path,'model_%05d.pth'%(start_epoch-1))
else:
    snapshot_path=None
