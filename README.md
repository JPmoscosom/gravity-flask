gcloud builds submit --tag gcr.io/gravity-419021/gravity --project=gravity-419021

gcloud run deploy gravity --image gcr.io/gravity-419021/gravity --platform managed --project=gravity-419021 --allow-unauthenticated --region us-east1

gcloud iam service-accounts list --project=gravity-419021

gcloud iam service-accounts keys create ./keys.json --iam-account  github-actions@gravity-419021.iam.gserviceaccount.com

gcloud auth activate-service-account --key-file=keys

gcloud beta compute health-checks create http healthcheck-produccion --project=gravity-419021 --port=8080 --request-path=/health --proxy-header=NONE --no-enable-logging --check-interval=30 --timeout=10 --unhealthy-threshold=2 --healthy-threshold=2

gcloud beta compute health-checks create tcp healtcheck-api-gravity --project=gravity-419021 --port=80 --proxy-header=NONE --no-enable-logging --check-interval=30 --timeout=10 --unhealthy-threshold=2 --healthy-threshold=2