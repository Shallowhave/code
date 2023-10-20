---
date created: 2023-09-14 09:59
date updated: 2023-09-14 10:14
---

## 基础配置

> 搭建环境：`centos7.9` 内核版本:`5.4.256`

```bash
# 将 SELinux 设置为 permissive 模式（相当于将其禁用）
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config

# 关闭防火墙
systemctl disable --now firewalld

# 关闭swap分区
swapoff -a
sed -i '/swap/s/^/#/' /etc/fstab

# 转发 IPv4 并让 iptables 看到桥接流量
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

# 加载模块
sudo modprobe overlay
sudo modprobe br_netfilter

# 设置所需的 sysctl 参数，参数在重新启动后保持不变
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

# 应用 sysctl 参数而不重新启动
sudo sysctl --system

# 在/etc/hosts/ 中添加 matser节点和node节点的解析
```

## 安装容器运行时环境

```bash
# containerd下载地址 https://github.com/containerd/containerd/releases
tar Cxzvf containerd-<VERSION>-<OS>-<ARCH>.tar.gz

# 使用systemd管理containerd
##  下载containerd service文件
wget -O /usr/lib/systemd/system/containerd.service https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
systemctl daemon-reload
systemctl enable --now containerd

# 安装runc插件
# runc下载地址 https://github.com/opencontainers/runc/releases
install -m 755 runc.amd64 /usr/local/sbin/runc

# 安装CNI插件
#CNI下载地址 https://github.com/containernetworking/plugins/releases
mkdir -p /opt/cni/bin
tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.1.1.tgz

# 生成containerd配置文件并修改参数
mkdir -p /etc/containerd
containerd config default > /etc/containerd/config.toml
sed -i 's/SystemdCgroup = false/SystemdCgroup = true/g' /etc/containerd/config.toml
systemctl restart containerd
```

## 安装Kubernetes

```shell
# 此操作会覆盖 /etc/yum.repos.d/kubernetes.repo 中现存的所有配置
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.28/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.28/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
EOF

# 安装 kubelet、kubeadm 和 kubectl，并启用 kubelet 以确保它在启动时自动启动
sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
sudo systemctl enable --now kubelet
```

## 使用kubadmin创建jiqun

```shell
kubadmin init 
```

## 安装calico网络插件

```bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

## 启用 shell 自动补全功能

```shell
# bash系统全局
kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl > /dev/null
sudo chmod a+r /etc/bash_completion.d/kubectl
```
