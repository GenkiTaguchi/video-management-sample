# Video Management Sample

## Purpose
Upload videos and metadata to Google Cloud Platform from your local node.

## Set up your local environment

Clone the [git repository](https://github.com/gtagheuer/video-management-sample) on your local node.

`💻 local`
```sh
git clone https://github.com/gtagheuer/video-management-sample.git
```

Create .env file on the cloned repository

`💻 local`
```sh
cd video-management-sample
touch .env
```
> **Warning**  
> ① DO NOT include any sensitive information or raw credentials in .env file if you push it to the repository.  
> ② DO NOT push .env file to the repository if you include the sensitive information or raw credentials in it.

## Set up your Google Cloud environment

Go to [Google Cloud](https://console.cloud.google.com/) and create a project for this prototyping.

Open your Cloud Shell and set your project ID.

```sh
gcloud config set project YOUR-PROJECT-ID
gcloud auth application-default login
```

Set environment variables.

```sh
source .envrc
```

Enable services.

```sh
gcloud services enable \
  storage.googleapis.com \
  pubsub.googleapis.com
```

### Configure Service Accounts
Create a service account for video-management service.

```sh
gcloud iam service-accounts create video-management
```

Create a service account key.
> **Warning**  
> Only run this command in case you have no other way to authenticate on-premise machines and you want to manage the keys programmatically.

```sh
gcloud iam service-accounts keys create ~/sa-private-key.json \
    --iam-account=video-management@${PROJECT_ID}.iam.gserviceaccount.com
```

Copy the content of the service account key onto your local node.

`💻 local`
```sh
mkdir service_account_keys
cd service_account_keys/
vim sa-private-key.json
cd ..
```

Edit .env file on your local node and set the service account key as your default Google Cloud credentials.

`💻 local`
```sh
GOOGLE_APPLICATION_CREDENTIALS=./service_account_keys/sa-private-key.json
```

Go back to your Cloud Shell and remove the key.

```sh
rm sa-private-key.json
```

### Configure Cloud Storage
Create a storage bucket.

```sh
gsutil mb gs://${PROJECT_ID}-videos
```

Add an “Object Creator” role to the service account for the storage bucket you just created.

```sh
gsutil iam ch \
  "serviceAccount:video-management@${PROJECT_ID}.iam.gserviceaccount.com:objectCreator" \
  gs://${PROJECT_ID}-videos
```

Edit .env file on your local node and set the bucket name.

`💻 local`
```sh
BUCKET_NAME=YOUR_PROJECT_ID-videos
```

Now you can upload the file from your local node to Cloud Storage.

`💻 local`
```sh
python upload_test.py
```













