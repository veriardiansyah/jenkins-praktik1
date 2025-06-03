pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }
        stage('Deploy') {
            when {
                aniOf {
                    branch 'master'
                    branch pattern: "release/.*", comparator: "REGEXP"
                }
            }
            steps {
                echo "Simulating deploy from branch ${env.BRANCh}"
            }
        }
    }

    post {
        success {
            script {
                def payload = [
                    content: "✅ Build SUCCESS on '${env.BRANCH_NAME}' URL: '${env.BUILD_URL}'"
                ]
                httpRequest(
                    httpMode: 'POST',
                    contentType: 'APPLICATION_JSON',
                    requestBody: groovy.json.JsonOutput.toJson(payload),
                    url: 'https://discord.com/api/webhooks/1379391196966817846/gPO0c3GQhA3BmOhbyD63esnrDC16SBDFNIFIuvbootsXlaNqnOr8-aC20c0oyGwHDnXU'
                )
            }
        }
        failure {
            script {
                def payload = [
                    content: "❌ Build FAILED on '${env.BRANCH_NAME}' URL: '${env.BUILD_URL}'"
                ]
                httpRequest(
                    httpMode: 'POST',
                    contentType: 'APPLICATION_JSON',
                    requestBody: groovy.json.JsonOutput.toJson(payload),
                    url: 'https://discord.com/api/webhooks/1379391196966817846/gPO0c3GQhA3BmOhbyD63esnrDC16SBDFNIFIuvbootsXlaNqnOr8-aC20c0oyGwHDnXU'
                )
            }
        }
    }
}