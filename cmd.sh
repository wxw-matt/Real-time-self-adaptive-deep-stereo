base_path="$HOME/Downloads/pretrained_nets/"
if [ -d model_data ];
then
  echo "model_data exists"
else
  mkdir -p model_data
  cp $base_path/MADNet/kitti/weights.ckpt.data-00000-of-00001 model_data/model.ckpt.data-00000-of-00001
  cp $base_path/MADNet/kitti/weights.ckpt.index model_data/model.ckpt.index
  cp $base_path/MADNet/kitti/weights.ckpt.meta model_data/model.ckpt.meta
fi
python make_example_list_with_gt.py
#python Stereo_Online_Adaptation.py \
#  --weights model_data/model.ckpt \
#  --modelName MADNet \
#  --blockConfig block_config/MadNet_full.json \
#  --sampleMode FIXED
#  -o output_test \
#  --list sample.csv

python Stereo_Online_Adaptation.py \
  --list sample.csv \
  -o output_test \
  --weights model_data/model.ckpt \
  --modelName MADNet\
  --blockConfig block_config/MadNet_full.json \
  --sampleMode PROBABILITY\
  --logDispStep 1
