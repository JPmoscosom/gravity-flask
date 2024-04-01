gcloud builds submit --tag gcr.io/gravity-419021/gravity --project=gravity-419021

gcloud run deploy gravity --image gcr.io/gravity-419021/gravity --platform managed --project=gravity-419021 --allow-unauthenticated --region us-east1

gcloud iam service-accounts list --project=gravity-419021

gcloud iam service-accounts keys create ./keys.json --iam-account  github-actions@gravity-419021.iam.gserviceaccount.com

gcloud auth activate-service-account --key-file=keys.json