import Augmentor

p = Augmentor.Pipeline('/home/carlos/Descargas/GITHUB/Inference_Project/src/data_collection/mango')

p.rotate90(probability=0.5)
p.rotate270(probability=0.5)
p.flip_left_right(probability=0.8)
p.flip_top_bottom(probability=0.3)
p.crop_random(probability=1, percentage_area=0.7)
p.resize(probability=1.0, width=128, height=128)
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)

p.sample(6000)
