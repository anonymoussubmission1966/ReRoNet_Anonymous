# Setup

## Download Model Checkpoints & Predictions

Due to GitHub file size limits, pre-trained model weights (`best_dice.pth`) and the actual output predictions are hosted on Google Drive. 

📁 **[Download Models & Predictions from Google Drive](https://drive.google.com/drive/folders/108yqEBPiyfMImbNao9bamQDJDLDOe6I4?usp=sharing)**

### Available Weights & Models

Place the downloaded `.pth` files into their respective directory inside your project root or `ckpts/` folder:

| Directory / Model Key | Model Description |
| :--- | :--- |
| `LW_UNET_TVERSKY` | Lightweight U-Net trained with Tversky Loss *(Generates ROI Mask)* |
| `RUN_FNO` | **ReRoNet** (Full Proposed Model with Fourier Neural Operator) |
| `RUN_CNN` | **ReRoNet Baseline** (CNN Counterpart without FNO) |
| `RUN_NO_COORD` | **ReRoNet Ablation** (Without Coordinate Convolutions) |
| `SWIN_RUN_LOCAL` | **SwinUNETR Baseline** |

### Actual Output Predictions (`eval_preds`)
The actual inference outputs (predictions) from the models are available in the **`eval_preds/`** folder on Google Drive. 

Because these prediction files are exceptionally large, it is not recommended to push them to GitHub. If you want to compute evaluation metrics or visualize the results without re-running the models yourself, simply download the `eval_preds` folder directly from the Drive link and place it in your project root.