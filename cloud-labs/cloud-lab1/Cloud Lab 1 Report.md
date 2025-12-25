## Лабораторная работа 1. Знакомство с IaaS, PaaS, SaaS сервисами в облаке на примере Amazon Web Services (AWS). Создание сервисной модели.
### Вариант 8
___
### 1. Цель работы
Изучить уровни абстракции облачных сервисов (IaaS, PaaS, SaaS) и на практике разобраться с моделью потребления ресурсов в AWS. В ходе выполнения необходимо проанализировать данные биллинга и классифицировать usage‑типы по иерархии сервисной модели.

____
### 2. Теория
#### 2.1. Модели предоставления облачных сервисов
**IaaS (Infrastructure as a Service)** – модель, в которой провайдер предоставляет базовую инфраструктуру: виртуальные машины, сети, хранилища, балансировщики. Пользователь управляет операционной системой, приложениями и данными.
Примеры: Amazon EC2, Amazon EBS, Amazon VPC.

**PaaS (Platform as a Service)** – платформа для разработки и запуска приложений без необходимости управлять серверами и ОС. Пользователь работает только с кодом и конфигурацией.
Примеры: AWS Lambda, AWS Elastic Beanstalk, Amazon RDS.

**SaaS (Software as a Service)** – полностью готовые приложения, предоставляемые по подписке. Пользователь работает только с функциональностью сервиса.
Примеры: Amazon WorkMail, Amazon Chime.

#### 2.2. Структура данных AWS Billing
**Product Code** – идентификатор сервиса AWS, к которому относится расход. Например: AmazonS3, AmazonDynamoDB, AmazonEKS.

**Usage Type** – строковый шаблон, описывающий конкретную метрику потребления: количество запросов, объём хранения, время работы, трафик и т.д. Символ `%` в начале или конце означает, что перед/после него может быть произвольная последовательность символов.

**Operation / LineItemDescription** – дополнительные поля, уточняющие тип операции (например, CreateFileSystem:Windows).

#### 2.3. Сервисная модель классификации
Используется иерархическая модель:
**IT Tower** – верхний уровень, отражающий технологическую область (Storage, Security, Compute, Database, AI/ML и др.).

**Service Family** – семейство сервисов внутри области (например, Storage&Content Delivery, Security and Identity, Containers & Orchestration).

**Service Type** – конкретный сервис AWS (Amazon S3, Amazon EKS, Amazon SageMaker).

**Service Sub Type** – функциональная категория внутри сервиса (Requests, Storage, Compute Node, Training, Backup и т.д.).

**Service Usage Type** – наиболее детальный уровень, соответствующий конкретной метрике биллинга (Tier 1 Requests, Fargate vCPU-Hours, Labeled Objects).

___
### 3. Исходные данные
Дан файл `Mapping Rules AWS team 8.csv` с фрагментом данных биллинга Amazon Web Services, который нужно импортировать в Excel-таблицу и классифицировать по иерархии сервисной модели:

IT Tower → Service Family → Service Type → Service Sub Type → Service Usage Type

___
### 4. Ход работы
Исходный CSV‑файл был импортирован в Excel для последующей обработки. Далее для каждого значения `Product Code` и `Usage Type` определялись соответствующие уровни сервисной модели: **IT Tower**, **Service Family**, **Service Type**, **Service Sub Type** и **Service Usage Type**. Классификация выполнялась на основе официальной документации AWS (https://docs.aws.amazon.com/) и функционального назначения сервисов. После заполнения всех полей была сформирована итоговая таблица, отражающая структуру потребления облачных ресурсов.

___
### 5. Классификация сервисов AWS
**Storage:**
- **Amazon FSx** (Throughput Capacity, Storage, Backup, Regional Data Transfer)
- **Amazon Glacier** (Storage Bytes, Provisioned Capacity, Timed Storage, Requests Tier 1/3, Early Delete)

**Security:**
- **Amazon GuardDuty** (Free/Paid Events Analyzed, Events Analyzed Bytes, Tax)
- **Amazon Inspector** (Agent Assessments, Network Assessments)

**Cloud Services/Application Hosting:**
- **AWS Amplify** (Data Transfer Out, Build Duration)

**Backup & Recovery:**
- **AWS Backup** (Cold/Warm Storage, Restore Cold/Warm, Early Delete Cold)

**Database:**
- **Amazon DAX** (Node Usage)
- **Amazon DynamoDB** (Read/Write Capacity Units, Read/Write Request Units, Streams Requests, Restore Data Size, Tax)

**Cloud Services/Containers & Orchestration:**
- **Amazon EKS** (Fargate vCPU-Hours, Fargate GB-Hours, EKS Cluster Hours, Tax)

**AI/ML:**
- **Amazon SageMaker** (Notebooks, Training, Processing, Batch Transform, Training Spot/Support, Hosting, Labeled Objects)

___
### 6. Вывод
В ходе лабораторной работы были проанализированы данные биллинга AWS и выполнена классификация usage‑типов по иерархии сервисной модели. Такой подход позволил структурировать потребление облачных ресурсов и понять, как различные сервисы относятся к уровням абстракции и функциональным областям. Построенная модель даёт возможность проводить дальнейший анализ затрат и формировать более прозрачное представление о структуре использования облачных сервисов.

___
