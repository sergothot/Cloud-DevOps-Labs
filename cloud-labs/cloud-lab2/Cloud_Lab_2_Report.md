## Лабораторная работа 2. Сравнение сервисов Amazon Web Services и Microsoft Azure. Создание единой кросс-провайдерной сервисной модели.

**Вариант 8**
___
### 1. Цель работы
Получить практические навыки анализа облачных сервисов разных провайдеров и построения единой кросс‑провайдерной сервисной модели. В ходе работы необходимо классифицировать usage‑типы Microsoft Azure по той же иерархии, которая была разработана в Лабораторной работе 1 для AWS, и выполнить сопоставление сервисов двух провайдеров.

____
### 2. Теория
#### 2.1. Модели предоставления облачных сервисов
**IaaS (Infrastructure as a Service)** – инфраструктурные сервисы: виртуальные машины, сети, хранилища, балансировщики. Примеры: Azure Virtual Machines, Azure Storage, Azure Load Balancer.

**PaaS (Platform as a Service)** – платформенные сервисы для разработки и запуска приложений. Примеры: Azure App Service, Azure Functions, Azure SQL Database.

**SaaS (Software as a Service)** – готовые приложения, предоставляемые по подписке. Примеры: Microsoft 365, Dynamics 365.

#### 2.2. Структура данных Azure Billing
**Meter Category / Sub‑Category / Meter Name** – параметры, описывающие тип потребления: вычисления, хранение, трафик, операции, лицензии и т.д.

**Consumed Service** – сервис Azure, которому принадлежит расход (например, Microsoft.Storage, Microsoft.Web, Microsoft.Devices).

#### 2.3. Сервисная модель классификации
Используется та же иерархия, что и в ЛР1:

IT Tower → Service Family → Service Type → Service Sub Type → Service Usage Type

Сохраняем модель, разработанную в ЛР1, т.е. используем те же IT Tower и те же Service Family:

- **IT Tower:** Storage, Security, Support, Database, Cloud Services, Compute
- **Service Family:** Storage & Content Delivery, Security and Identity, Mobile Services, Management Tools, Database, Compute, Artificial Intelligence

___
### 3. Исходные данные
Дан файл `Azure lab team 8.csv` с фрагментом данных биллинга Microsoft Azure. Необходимо классифицировать каждую строку по пяти уровням сервисной модели, сохранив логику, выработанную в ЛР1.

___
### 4. Ход работы
CSV‑файл был импортирован в Excel. Для каждого значения `Consumed Service`, `Meter Category` и `Meter Name` определялись уровни сервисной модели: **IT Tower**, **Service Family**, **Service Type**, **Service Sub Type**, **Service Usage Type**. Классификация выполнялась на основе официальной документации Azure (https://learn.microsoft.com/en-us/azure/) и сопоставления функциональности сервисов с моделью, разработанной в ЛР1.

___
### 5. Классификация сервисов AWS
**Storage:**
- **Azure Storage** (General Storage)
- **Data Transfer Out**
- **Standard IO (Table/Queue)**
- **Standard IO (Page Blob/Disk)**
- **Azure CDN** (Data Transfer)
- **Media Services** (Media Processing)

**Security:**
- **Active Directory B2C** (Basic Authentications)
- **Virtual Machines Licenses** (License Charges)

**Cloud Services:**
- **Dynamics Customer Insights** (Standard S1)
- **SignalR Service** (Realtime Messaging)
- **IoT Hub** (Device Messaging)
- **Websites** (Free Tier, IP SSL)
- **Azure Marketplace** (Third‑party Services)

**Support/Management:**
- **Azure Site Recovery** (VM Replication)
- **Event Grid** (Operations)
- **Load Balancer** (Batch / ML / Network)
- **Visual Studio Team Services** (Users)
- **Visual Studio Build and Deployment** (Private Agents, Hosted Agents)
- **Application Insights** (Telemetry)

**Database:**
- **Windows Azure Service Bus (SQL)**

**Compute:**
- **Container Instances** (Duration Hours)
- **Virtual Machines** (RHEL, SQL Server, BizTalk, Java Dev Env, Reservation)
- **Websites – Compute Hours**
- **Cognitive Services – QnA Maker** (QnA Requests)

___
### 6. Сравнение AWS и Azure
Построив классификацию для обоих провайдеров, можно выделить следующие наблюдения:
- **Product Code (AWS)** и **Consumed Service (Azure)** выполняют одинаковую роль – однозначно определяют сервис.
- **Usage Type (AWS)** и **Meter Name (Azure)** описывают конкретную метрику потребления.
- Сервисы обоих провайдеров можно объединить в схожие категории: Compute, Storage, Database, Security, Support, Cloud Services.
- Azure разделяет метрики на Meter Category и Meter Sub‑Category, а AWS использует более длинные шаблоны Usage Type.
- Сетевые сервисы Azure (Load Balancer, Virtual Network) можно логично вписать в Service Family **Management Tools**, т.к. в модели из ЛР1 нет отдельной группы Networking.

___
### 7. Вывод
В ходе лабораторной работы была выполнена классификация usage‑типов Microsoft Azure по той же иерархической модели, что и в ЛР1 для AWS. Это позволило сформировать единое кросс‑провайдерное представление о структуре облачных сервисов и сопоставить функциональные области двух платформ.

___
