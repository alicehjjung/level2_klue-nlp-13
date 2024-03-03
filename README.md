# level2_klue-nlp-13
[ENG](#ENG)   
[한국어](#한국어)

## ENG
# Relation Extraction(RE) project
This project identifies semantic relations between entity pairs in a text.<br>
We used a pre-trained model from the Hugging Face and KLUE-RE dataset and trained the pre-trained model to predict the relations between the subject and object entity.<br>
[Furter information about KLUE-RE](https://klue-benchmark.com/tasks/70/overview/description)<br>

## Getting Started

To use this project, follow these steps:

### Train and Test the Model
```
python main.py
```

## 한국어
## ✅ 목차
[1. 정보](##-📜-정보) > [2. 진행 과정](##-진행-과정) > [3. 팀원](##-팀원) > [4. 역할](##-역할) > [5. 디렉토리 구조](##-%EB%94%94%EB%A0%89%ED%86%A0%EB%A6%AC-%EA%B5%AC%EC%A1%B0) > [6. 프로젝트 구성](##-프로젝트-구성)

➡️ [랩업 리포트 보기](https://docs.google.com/document/d/1dwhaQoOnZzl3s6F2vtphMKYjMa3eUJluh2rG2iNrIuA/edit#)
<br>

## 📜 정보
- 주제 : 부스트캠프 5기 Level 2 프로젝트 - 문장 내 개체간 관계 추출(KLUE RE)
- 프로젝트 기간 : 2023년 5월 2일 ~ 2023년 5월 18일
- 프로젝트 내용 : Hugging Face의 Pretrained 모델과KLUE RE 데이터셋을 활용해 주어진 subject, object entity간의 30개 중 하나의 relation 예측하는 AI 모델 구축

<br>

## 🗓️ 진행 과정

![ganttchart](https://github.com/boostcampaitech5/level2_klue-nlp-13/assets/42113966/41e1218f-1efa-4959-b7c4-7ce40eeaf6b9)

<br>

## 👨🏼‍💻 팀원

<table>
    <tr height="160px">
        <td align="center" width="150px">
            <a href="https://github.com/Yunhee000"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/Yunhee000"/></a>
            <br/>
            <a href="https://github.com/Yunhee000"><strong>김윤희</strong></a>
            <br />
        </td>
        <td align="center" width="150px">
            <a href="https://github.com/8804who"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/8804who"/></a>
            <br/>
            <a href="https://github.com/8804who"><strong>김주성</strong></a>
            <br />
        </td>
        <td align="center" width="150px">
            <a href="https://github.com/ella0106"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/ella0106"/></a>
            <br/>
            <a href="https://github.com/ella0106"><strong>박지연</strong></a>
            <br />
        </td>
        <td align="center" width="150px">
            <a href="https://github.com/bom1215"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/bom1215"/></a>
            <br/>
            <a href="https://github.com/bom1215"><strong>이준범</strong></a>
            <br />
        </td>
        <td align="center" width="150px">
            <a href="https://github.com/HYOJUNG08"><img height="120px" width="120px" src="https://avatars.githubusercontent.com/HYOJUNG08"/></a>
            <br/>
            <a href="https://github.com/HYOJUNG08"><strong>정효정</strong></a>
            <br />
        </td>
    </tr>
</table>
<br>

## 🧑🏻‍🔧 역할

| 이름 | 역할 |
| :----: | --- |
| **김윤희** | 데이터 전처리(entity token), 품사 태깅, 모델 성능 실험 |
| **김주성** | 코드 모듈화, 데이터 증강(RD, MLM),  모델 성능 실험 |
| **박지연** | 코드 모듈화, Wandb 추가, concat entity 실험 |
| **이준범** | EDA, 데이터 증강(Easy Data Aug), 기능 추가 |
| **정효정** | 모델 리서치, 데이터증강(역번역), 데이터 전처리(Typed entity marker (punct)) |

<br>

## 📁 디렉토리 구조

```bash
├── level2_KLUE-nlp-13
|   ├── basecode/ (private)
│   ├── data/ (private)
│   ├── results/ (private)
│   ├── eda/
│   ├── utils/
│   │   ├── DataAugmentation.py
│   │   ├── DataLoader.py
│   │   ├── Dataset.py
│   │   ├── DataPreprocessing.py
│   │   ├── Inference.py
│   │   ├── Model.py
│   │   ├── R_RoBERTa_model.py
│   │   ├── Score.py
│   │   ├── Train.py
│   │   ├── Utils.py
│   │   ├── backtranslation.ipynb
│   │   ├── customModel.py
│   │   ├── dict_label_to_num.pkl
│   │   └── dict_num_to_label.pkl
│   ├── main.py
│   ├── README.md
│   ├── config.yaml
|   ├── sweep.py
│   └── data_processing.py
```
<br>

## ⚙️ 프로젝트 구성

|분류|내용|
|:--:|--|
|데이터|• `raw data` : 기본 train 데이터 32470개 |
|모델|• [`klue/bert-base`](https://huggingface.co/klue/bert-base), [`klue/roberta-large`](https://huggingface.co/klue/roberta-large), `HuggingFace Transformer Model`+`Pytorch Lightning`활용 + biLSTM Layer 추가 , RBERT 모델 구조 활용|
|전처리|• `Entity Token` : Entity marker / Type marker / Typed entity marker / SUB,OBJ marker / punct(한글) 등 다양한 entity representation을 적용하여 최적의 성능을 내는 entity representation 적용 |
|증강|• Easy Data Augmentation, Back Translation, MLM Model, 문장 유사도 측정으로 증강, 품사 태깅으로 증강, Label & Entity 같은 행 서로 단어 교체|
|앙상블 방법|• `micro F1`과 `auprc` 각각 기준으로 점수가 높았던 모델들로 soft voting 진행|
|모델 성능 개선 노력|• Learning Rate Scheduling, Focal Loss 적용, fp16으로 학습 속도 향상, confusion matrix로 모델 성능 평가|

<br>
