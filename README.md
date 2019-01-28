kube-resource
=============

Manages Kubernetes resources based on a set of manifest templates

The kube-resource role implements the principles of immutable configmaps
and secrets as
[presented at AnsibleFest 2018](https://www.ansible.com/managing-kubernetes-is-easy-with-ansible)

Requirements
------------

* openshift 0.8.2
* kubernetes-validate (only needed if `kube_resource_validation_options` is set

Role Variables
--------------

* `kube_resource_namespace` - namespace in which to create resources
* `kube_resource_name` - name of resource being managed
* `kube_resource_configmaps` - a dict of ConfigMaps, mapping a reference name to a ConfigMap definition
* `kube_resource_manifest_files` - a list of resource definition template file names
* `kube_resource_secrets` - a dict of Secrets, mapping a reference name to a Secret definition
* `kube_resource_secrets_files` - a list of Secret definition template file names
* `kube_resource_UNSAFE_show_logs` - whether to show the logs when working with secrets. Defaults to `no`.
  For use when troubleshooting problems with secret definitions.
* `kube_resource_validate_options` - how to validate Kubernetes resources. Defaults to an empty dict,
  disabling validation. A sensible setting is:
  ```
  kube_resource_validate_options:
    strict: yes
    fail_on_error: yes
  ```
* `kube_resource_wait` - whether to wait for resources to reach their desired state (default `no`)
* `kube_resource_wait_timeout` - how long to wait in seconds for resources if `kube_resource_wait` is on
  (default 120)


Dependencies
------------

None

Example Playbook
----------------

```
kube_resource_configmaps:
  my-resource-env: "{{ lookup('template', template_dir + '/my-resource-env.j2') }}"
```

```
kube_resource_manifest_files: "{{ lookup('fileglob', template_dir + '/*manifest.yml') }}"
```

```
- hosts: "{{ application }}-{{ env }}-runner"
  roles:
    - kube-resource
```

The molecule/default directory now contains a working playbook and inventory suitable for
running on Kubernetes for Docker

Testing
-------

The role comes with a [molecule](https://molecule.readthedocs.io/) test suite that should
work against any reasonable Kubernetes implementation (it has been tested against Kubernetes
for Docker)

```
K8S_AUTH_CONTEXT=docker-for-desktop molecule test
```

License
-------

BSD

Author Information
------------------

Will Thames (@willthames)
