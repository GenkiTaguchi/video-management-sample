# Video Management Sample

## Purpose
Create an application which uploads videos and metadata to Google Cloud Platform from local nodes.

## Set up your local environment

Clone the [git repository](https://github.com/GenkiTaguchi/video-management-sample) on your local node.

`💻 local`
```sh
git clone https://github.com/GenkiTaguchi/video-management-sample.git
```

Create .env file on the cloned repository

`💻 local`
```sh
cd video-management-sample
touch .env
```

## Set up your Google Cloud environment

Go to console.cloud.google.com and create a project for this prototyping.

Set your project ID.

`💭 cloud`
```sh
gcloud config set project YOUR-PROJECT-ID
gcloud auth application-default login
```

Set environment variables.

`💭 cloud`
```sh
source .envrc
```

Enable services.

`💭 cloud`
```sh
gcloud services enable \
  storage.googleapis.com \
  pubsub.googleapis.com \
```

### Configure Service Accounts
Create a service account for video-management service.

`💭 cloud`
```
gcloud iam service-accounts create video-management
```

**Warning**
Only run this command in case you have no other way to authenticate on-premise machines and you want to manage the keys programmatically.

Create a service account key

`💭 cloud`
```
gcloud iam service-accounts keys create ~/sa-private-key.json \
    --iam-account=video-management@${PROJECT_ID}.iam.gserviceaccount.com
```

Copy and paste the content of the service account key onto your local node, and then remove the key from your Cloud Shell.

`💭 cloud`
```
rm sa-private-key.json
```

Edit .env file on your local node and set the service account key as your default Google Cloud credentials.

`💭 cloud`
```
GOOGLE_APPLICATION_CREDENTIALS=./service_account_keys/sa-private-key.json
```

###Configure Cloud Storage
Create a storage bucket.

`💭 cloud`
```
gsutil mb gs://${PROJECT_ID}-videos
```

Add an “Object Creator” role to the service account for the storage bucket you just created.

`💭 cloud`
```
gsutil iam ch \ "serviceAccount:video-management@${PROJECT_ID}.iam.gserviceaccount.com:objectCreator" \
  gs://${PROJECT_ID}-videos
```

Edit .env file on your local node and set the bucket name.

`💻 local`
```
BUCKET_NAME=YOUR_PROJECT_ID-videos
```

Now you can upload the file from your local node to Cloud Storage.
Run ‘upload_test.py’

`💻 local`
```
python upload_test.py
```













