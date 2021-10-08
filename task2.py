from featureGenerator import save_features_to_json
import imageLoader
import modelFactory
import argparse
import numpy as np

from tech.SVD import SVD
from utilities import extract_type_weight_pairs, print_semantics_type

parser = argparse.ArgumentParser(description="Task 2")
parser.add_argument(
    "-fp",
    "--folder_path",
    type=str,
    required=True,
)
parser.add_argument(
    "-f",
    "--feature_model",
    type=str,
    required=True,
)
parser.add_argument(
    "-y",
    "--Y",
    type=str,
    required=True,
)

parser.add_argument(
    "-k",
    "--k",
    type=int,
    required=True,
)
parser.add_argument(
    "-t",
    "--tech",
    type=str,
    required=True,
)
args = parser.parse_args()

data = imageLoader.load_images_from_folder(args.folder_path,'*',args.Y)
if data is not None:
    model = modelFactory.get_model(args.feature_model)
    images = data[1]
    labels = data[0]
    features = model.compute_features_for_images(images)
    if(args.tech=='pca'):
        #PCA
        args.tech
    elif(args.tech=='svd'):
        svd = SVD(args.k)
        latent_data = svd.compute_semantics(features)
        print_semantics_type(labels,np.matmul(np.array(latent_data[0]),np.array(latent_data[1])))
        file_name = "latent_semantics_"+args.feature_model+"_"+args.tech+"_"+args.Y+"_"+str(args.k)+".json"
        save_features_to_json(args.folder_path,latent_data,file_name)
    elif(args.tech=='lda'):
        args.tech
    else:
        args.tech
