
### Pelican Static Site Continous Delivery to AWS S3 using github actions

This a template project that uses [Pelican](https://getpelican.com/) **Markdown** based static generator as a platform for your static site and generated HTML static files will be pushed to AWS S3.

This project eliminates the need to perform below steps and focus on creating the content in **Markdown**

- Running Pelican commands to generate static files
- Pushing the files manually to S3

This template project uses **github** actions to perform continous delivery for generated HTML to AWS S3.

**https://silverdedreamer.me** site was generated using the similar approch.

##### Prerequisites
- This article assumes you already have static site hosted and running in amazon S3 and also you wanted to matain content **Markdown** and is maintained in github repository.
- Make sure you have AWS credentials required to run a CloudFormation template
- AWS Cloudformation minimum knowledge to run the template just one time.

### One Time Setup

##### Configure an AWS user to be used for github actions

To levarage github actions to do Continous Delivery and deploy the static files without touching any other code then we would need create an AWS user with very minimal set of privilages to be specifically used for github actions.

Simple and easy thing to do is AWS Cloudformation template and just run a single command to generate required AWS resource . Thanks to this [user](https://github.com/antklim) who has created the template. All we need to do is just run a below command and gathers the required AWS ACCESS KEY and AWS SECRET KEY

Please refer to [this](https://github.com/antklim/gh-actions-user) on how to use the AWS cloud formation template to create a AWS user.
```

aws cloudformation create-stack --stack-name gh-actions-user \
  --template-body file://main.yml \
  --parameters ParameterKey=AssetsBucket,ParameterValue=my-assets-bucket \
  ParameterKey=ExternalId,ParameterValue=ExternalID \
  ParameterKey=ProjectName,ParameterValue=MyProject \
  --tags Key=project,Value=MyProject \
  --region ap-southeast-2 \
  --capabilities CAPABILITY_NAMED_IAM \
  --output yaml \
  --profile my-profile
  
```

Pls gather below details after executing cloudformation template

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_ROLE_TO_ASSUME
- AWS_ROLE_EXTERNAL_ID
- AWS_REGION
- BUCKET_NAME

###### Configure github to use the AWS user

On the the repo where you have your static content hosted , configure the AWS credentials gathered in the previous step as shown below
<img src="/images/github-secrets.png" alt="gitlab Secret" title="gitlab Secret">

#### Configure github workflow for Continuous Delivery to S3

Go your repository , Go to Actions Menu , Click on New Workflow
<img src="/images/github-actions-new-workflow.PNG" alt="Workflow" title="Workflow">




Copy paste below code ,pls refer [here](https://raw.githubusercontent.com/sdontireddy/pelican-static-site-continuous-delivery-to-aws-s3/main/.github/workflows/publish-pelican-site-to-aws-s3.yml) for the contents.

```

## Install and trigger Pelican publish
name: Trigger Make

on:
  push:
    branches: [ main ]

jobs:
  deploy:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      env:
        BUCKET_NAME: ${{ secrets.BUCKET_NAME }}
        AWS_ACCESS_KEY_ID : ${{ secrets.AWS_ACCESS_KEY_ID }}
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install pelican
        
        python -m pip install "pelican[markdown]"
        #Pls change to whatever Pelican you want to install
        git clone https://github.com/alexandrevicenzi/Flex
        pelican-themes --install Flex/ --verbose
        pelican-themes -l
                
    - name: Generate OutPutfolder
      run: |
        echo $BUCKET_NAME
        make publish
    - name: Upload outputfolder 
      uses: actions/upload-artifact@master
      with:
        name: outputfolder
        path: ./output/
  upload:
    name: Upload assets to S3 bucket
    needs: [deploy]
    runs-on: ubuntu-latest
    steps:
    - uses: actions/download-artifact@master
      with:
        name: outputfolder
        path: ./output/
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region:  ${{ secrets.AWS_REGION }}
        role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
        role-external-id: ${{ secrets.AWS_ROLE_EXTERNAL_ID }}
        role-duration-seconds: 1200
        role-session-name: AssetsUploadSession
    - name: Copy files to S3 bucket
      run: |
        ls
        aws s3 sync output/ s3://${{ secrets.BUCKET_NAME }}


```



Note : Default **Flex** Pelican template is used.If you need to chage , pls do change Line 99 in above file.

Thats it! You have a github repository to manage content in markdown , whenever you push new code to **main** branch your content in **Markdown** will be converted to Static HTML and deployed to S3 bucket specified in the previous steps.
