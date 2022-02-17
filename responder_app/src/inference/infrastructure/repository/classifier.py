from typing import Any, Dict, Tuple
import torch
from torch import nn
from torch.nn.functional import softmax
from torchvision import transforms, models
from torchvision.models import ResNet
from torchvision.transforms.transforms import Compose
from inference.domain.object.content import Content
from inference.helper.api_module import logger


class Classifier(object):
    net: ResNet
    transformer: Compose
    config: Dict[str, Any]

    def __init__(self, model_path: str):
        self.__load_model(model_path)
        self.__build_transformer()

    def predict(self, content: Content) -> Tuple[int, float]:
        x = self.transformer(content.data)
        x = x.unsqueeze(0)  # type: ignore
        x.to('cpu')
        with torch.no_grad():
            outputs = self.net(x)

        _, preds = torch.max(outputs, 1)  # type: ignore
        label = int(preds)
        output = softmax(input=outputs, dim=1)[:, 1]
        score = float(output.cpu()) if label == 1 else 1 - float(output.cpu())
        confidence = float('{:.3f}'.format(score))
        return (label, confidence)

    def __load_model(self, model_path: str) -> None:
        device = 'cpu'
        state = torch.load(model_path, map_location=torch.device(device))
        self.net = models.resnet50(pretrained=False)
        self.config = state['configuration']
        self.net.fc = nn.Sequential(*[  # type: ignore
            nn.Dropout(p=self.config['dropout']),
            nn.Linear(self.net.fc.in_features, 2)]
        )
        self.net.load_state_dict(state['model'])
        self.net.to(device)
        self.net.eval()
        logger.info(f'loading classifier model: {model_path}')

    def __build_transformer(self) -> None:
        image_size = self.config['image_size']
        MEAN_IMAGE = [0.56927896, 0.5088081, 0.48382497]
        STD_IMAGE = [0.27686155, 0.27230453, 0.2761136]
        self.transformer = transforms.Compose([
            transforms.Resize((image_size, image_size)),
            # transforms.CenterCrop(image_size),
            transforms.ToTensor(),
            transforms.Normalize(MEAN_IMAGE, STD_IMAGE)
        ])
