import os
import subprocess
import sys
import warnings

warnings.filterwarnings("ignore")


def test_01():

    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Test if the homework script runs without errors
    try:
        for model in ["elasticnet", "knn"]:
            subprocess.run(
                [sys.executable, "-m", "homework", "--model", model],
                check=True,
                cwd=project_root,
            )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    # Ensure the mlruns directory exists
    mlruns_path = os.path.join(project_root, "mlruns")
    assert os.path.exists(mlruns_path), "mlruns directory does not exist."

    # Check if there are any experiments saved in mlruns/
    experiments = [
        d
        for d in os.listdir(mlruns_path)
        if os.path.isdir(os.path.join(mlruns_path, d))
    ]
    assert len(experiments) > 0, "No experiments found in mlruns directory."

    # Check if the required file exists
    make_predictions_path = os.path.join(project_root, "make_predictions.py")
    assert os.path.exists(
        make_predictions_path
    ), "make_predictions.py file does not exist."
