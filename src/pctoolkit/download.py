import os
import gdown

# Example mapping of model names to their Google Drive URLs
MODEL_URLS = {
    "gigaword-L8": "https://drive.google.com/drive/folders/1BTf9wLjth0usCOT1WxoL4FSC2EYBeO3z",
    "newsroom-L11": "https://drive.google.com/drive/folders/1qC6eo2-9H9U4Yi09x5vw6oFCvosSaivK",
    "newsroom-L75": "https://drive.google.com/drive/folders/14jsz1MiVpGh5vS5c5j43qRd1hQc7t7Nr",
    # Add more models as needed
}

DOWNLOAD_DIR = os.path.expanduser(
    "~/pctoolkit_models"
)  # Predefined folder to store the models


def download_model(model_name: str, download_dir: str = DOWNLOAD_DIR):
    output_path = os.path.join(download_dir, model_name)

    if os.path.exists(output_path):
        print(f"Model {model_name} is already downloaded in {output_path}.")
        return

    if model_name not in MODEL_URLS:
        print(f"Model {model_name} is not available.")
        return

    url = MODEL_URLS[model_name]
    os.makedirs(output_path, exist_ok=True)
    gdown.download_folder(url, output=output_path, quiet=False)
    print(f"Model {model_name} downloaded to {output_path}")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Download and install pctoolkit models"
    )
    parser.add_argument("model", type=str, help="Name of the model to download")
    args = parser.parse_args()

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    download_model(args.model)


if __name__ == "__main__":
    main()
