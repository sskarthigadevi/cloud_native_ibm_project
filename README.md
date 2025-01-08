# Cloud-Native Application Development with IBM Cloud and Kubernetes

## Overview
This project demonstrates deploying a cloud-native application using IBM Cloud and Kubernetes.

### Steps

1. **Setup IBM Cloud**
   - Provision a Kubernetes cluster on IBM Cloud.
   - Install the IBM Cloud CLI and Kubernetes CLI:
     ```bash
     ibmcloud login
     ibmcloud ks cluster config --cluster <cluster-name>
     ```

2. **Build and Push Docker Image**:
   - Build the Docker image:
     ```bash
     docker build -t karthigaadevi12/cloud-native-app:latest .
     ```
   - Push the Docker image to DockerHub:
     ```bash
     docker push karthigaadevi12/cloud-native-app:latest
     ```

3. **Deploy Application to Kubernetes**:
   - Apply deployment and service configurations:
     ```bash
     kubectl apply -f deployment.yaml
     kubectl apply -f service.yaml
     ```
   - Deploy using Helm (optional):
     ```bash
     helm install cloud-native-app ./helm_chart
     ```

4. **Monitor and Visualize**:
   - Deploy Prometheus and Grafana for monitoring:
     ```bash
     kubectl apply -f monitoring/prometheus-config.yaml
     kubectl apply -f monitoring/grafana-dashboard.json
     ```
   - Access Grafana dashboards and Prometheus metrics using Kubernetes service details.

5. **Set Up Service Mesh**:
   - Install Istio on your cluster:
     ```bash
     istioctl install
     ```
   - Apply Istio configuration for traffic management:
     ```bash
     kubectl apply -f istio-config.yaml
     ```

6. **Provision Infrastructure with Terraform**:
   - Navigate to the Terraform directory:
     ```bash
     cd terraform
     ```
   - Initialize Terraform and apply the configuration:
     ```bash
     terraform init
     terraform apply
     ```