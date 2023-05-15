# Heimatkunde dataset
Multi-modal layout analysis and classification dataset.

## Experiments

Experiments performed on this dataset are hosted on a different GitHub repository, which can be accessed here: https://github.com/honzikv/multimodal-document-processing-thesis

## Structure

The root of the repository constitutes the root of the dataset. The structure is as follows:

- `images` - default folder for COCO images
- `test.json` and `train.json` are the COCO annotations for the test and train splits respectively. These files are usable e.g. in Detectron2 for instance segmentation or object detection.
- `classifier` - contains the classification dataset, which are mapped annotations to our custom format that is loadable with scripts from our experiments
- `yolo` - contains the YOLO annotations for the dataset which are also applicable to object detection or instance segmentation
- `ocr` - contains the OCR annotations for the dataset
