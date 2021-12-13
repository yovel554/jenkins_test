#!/usr/bin/python3
pipeline {
        agent any
        stages {
            stage('build') {
                steps {
                    sh 'python pip install -m pytest'
                    }
                }
            stage ('Test'){
                steps "
                sh 'python3 test_add.py'
                }
                }
                }
