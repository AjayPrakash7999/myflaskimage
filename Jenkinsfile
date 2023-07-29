pipeline{
    agent any
    stages{
        stage('SCM checkout'){
            steps{
            git branch: 'main', url: 'https://github.com/AjayPrakash7999/myimage.git'
            }
        }
        stage('docker image '){
            steps{
            sh '/usr/bin/docker image build -t ajayprakash/myflaskimage . '
            }
        }
        
        stage('login autho '){
            steps{
           sh 'echo dckr_pat_K5TZg0aUvuzypMOf-GBvhFnkpho | docker login -u ajayprakash --password-stdin'
            }   
     
        }
        stage(' push image '){
                steps{
                sh '/usr/bin/docker image push ajayprakash/myflaskimage'
                }   
        }
        
        stage(' remove exitising ser '){
                steps{
                sh '/usr/bin/docker service rm service1'
                }   
        }
        
        stage(' create service '){
                steps{
                sh '/usr/bin/docker service create --name service1 -p 4000:4000 --replicas 2 ajayprakash/myflaskimage'
                }   
        }
        
        
    }
    
        
}
