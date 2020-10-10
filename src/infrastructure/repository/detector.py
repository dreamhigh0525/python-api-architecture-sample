from typing import Any, Dict, Tuple
import torch
from torchvision.models.detection.faster_rcnn import FasterRCNN, fasterrcnn_resnet50_fpn
from torchvision.transforms import transforms
from torchvision.transforms.transforms import Compose
from src.domain.object.content import Content


class Detector(object):
    net: FasterRCNN
    transformer: Compose
    config: Dict[str, Any]

    def __init__(self, model_path: str):
        self.__load_model(model_path)
        self.__build_transformer()

    def predict(self, content: Content) -> Tuple[int, float]:
        x = self.transformer(content.data)
        x = x.unsqueeze(0)
        x.to('cpu')
        with torch.no_grad():
            outputs = self.net(x)

        is_exists = len(outputs[0]['labels'])
        if is_exists > 0:
            label: int = outputs[0]['labels'].item()
            score: float = float('{:.3f}'.format(outputs[0]['scores'][0].item()))
        else:
            label = 0
            score = 0.0
        # [{'boxes': tensor([[ 66.9177, 158.3443, 110.1927, 182.2636]]), 'labels': tensor([1]), 'scores': tensor([0.9993])}]
        # resize_box_factors = [image.width / image_size, image.height / image_size] * 2
        # box = outputs[0]['boxes'][0]
        # resized_box = box.cpu() * torch.tensor(resize_box_factors)
        # box_xywh = resized_box[:2].tolist() + (resized_box[2:] - resized_box[:2]).tolist()
        # print(box_xywh)
        print(label, score)
        return (label, score)

    def __load_model(self, model_path: str) -> None:
        print('loading detector model')
        device = 'cpu'
        state_dict = torch.load(model_path, map_location=torch.device(device))
        labels_enumeration = state_dict['labels_enumeration']
        num_classes = len([key for key, val in labels_enumeration.items() if val >= 0])
        self.net = fasterrcnn_resnet50_fpn(pretrained_backbone=True, num_classes=num_classes)
        self.config = state_dict['configuration']
        self.net.load_state_dict(state_dict['model'])
        self.net.to(device)
        self.net.eval()

    def __build_transformer(self) -> None:
        image_size = self.config['image_size']
        self.transformer = transforms.Compose([
            transforms.Resize((image_size, image_size)),
            transforms.ToTensor(),
        ])
