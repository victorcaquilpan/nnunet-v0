import os
import subprocess

def main():
    # Set environment variables
    os.environ['nnUNet_raw'] = "/data/nnunet-environment/nnUNet_raw/"
    os.environ['nnUNet_preprocessed'] = "/data/nnunet-environment/nnUNet_preprocessed/"
    os.environ['nnUNet_results'] = "/data/nnunet-environment/nnUNet_results/"
    
    # Set the working directory
    workdir = "/workspace/nnunet-v0"
    os.chdir(workdir)
    
    # Add the directory to PYTHONPATH
    pythonpath = os.environ.get('PYTHONPATH', '')
    os.environ['PYTHONPATH'] = f"{workdir}:{pythonpath}"
    
    # Print PYTHONPATH for debugging purposes
    print(f"PYTHONPATH: {os.environ['PYTHONPATH']}")
    
    # # Run preprocessing 
    # preprocess_command = [
    #     "python", "./nnunetv2/experiment_planning/plan_and_preprocess_entrypoints.py",
    #     "-d", "2", "--verify_dataset_integrity"
    # ]
    # subprocess.run(preprocess_command, check=True)
    
    # Run training 
    training_command = [
        "python", "./nnunetv2/run/run_training.py",
        "2", "2d", "1", "--npz"
    ]
    subprocess.run(training_command, check=True)
    
    # Run inference
    # inference_command = [
    #     "python", "./nnunetv2/inference/predict_from_raw_data.py",
    #     "-i", "/data/nnunet-environment/nnUNet_raw/Dataset001_BrainTumourBrats2023/imagesTs/",
    #     "-o", "/data/nnunet-environment/predictions/",
    #     "-d", "1", "--save_probabilities",
    #     "-m", "/data/nnunet-environment/nnUNet_results/fold_0/checkpoint_best.pth"
    # ]
    #subprocess.run(inference_command, check=True)

    # Run inference
    # best_conf_command = [
    #     "python", "./nnunetv2/evaluation/find_best_configuration.py",
    #     "dataset_name_or_id", "1",
    # ]
    # subprocess.run(best_conf_command, check=True)


if __name__ == "__main__":
    main()