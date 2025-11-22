# register_cow_keypoints.py

import os
from detectron2.data.datasets import register_coco_instances
from detectron2.data import MetadataCatalog


# Replace this list with the exact keypoint names from your COCO JSON (order matters)
KEYPOINT_NAMES = [
"fknee","bknee","ffeet","bfeet","fthigh","bthigh","center","ucurve","lcurve","fmid","bmid","feye","seye","nose"
]




def register_cow_keypoints(train_json_path: str = "vali.json", train_images_dir: str = "tryx",
    val_json_path: str = "vali.json",
    val_images_dir: str = "tryx"):

# Basic sanity checks
    if not os.path.exists(train_json_path):
        raise FileNotFoundError(f"Train JSON not found: {train_json_path}")
    if not os.path.exists(train_images_dir):
        raise FileNotFoundError(f"Train images dir not found: {train_images_dir}")
    if not os.path.exists(val_json_path):
        raise FileNotFoundError(f"Val JSON not found: {val_json_path}")
    if not os.path.exists(val_images_dir):
        raise FileNotFoundError(f"Val images dir not found: {val_images_dir}")
    register_coco_instances("cow_train", {}, train_json_path, train_images_dir)
    register_coco_instances("cow_val", {}, val_json_path, val_images_dir)


# Set metadata for visualization / evaluation (ensure names/order match your JSON)
    MetadataCatalog.get("cow_train").set(
    thing_classes=["cow"],
    keypoint_names=KEYPOINT_NAMES,
    )
    MetadataCatalog.get("cow_val").set(
    thing_classes=["cow"],
    keypoint_names=KEYPOINT_NAMES,
    )




# If executed as a script, perform a quick registration and print metadata
if __name__ == "__main__":
    try:
        register_cow_keypoints()
        md = MetadataCatalog.get("cow_train")
        print("Registered cow_train and cow_val")
        print("Metadata: ", {"thing_classes": md.get('thing_classes'), "num_keypoints": len(md.get('keypoint_names', []))})
    except Exception as e:
        print("Registration failed:", e)