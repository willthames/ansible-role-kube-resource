kube-resource
=============

Manages Kubernetes resources based on a set of manifest templates

The kube-resource role implements the principles of immutable configmaps
and secrets as
[presented at AnsibleFest 2018](https://www.ansible.com/managing-kubernetes-is-easy-with-ansible)

Requirements
------------

* openshift 0.11.2 or above
* kubernetes-validate (only needed if `kube_resource_validation_options` is set
* kubernetes
* kubernetes-validate python module if `kube_resource_validate` is set
* community.kubernetes collection 1.0.0 (if using 2.10 onwards)

Role Variables
--------------

* `kube_resource_apply` - whether to use client side apply (equivalent to `kubectl apply`)
* `kube_resource_namespace` - namespace in which to create resources
* `kube_resource_create_namespace` - whether to create the namespace (defaults to `False`)
* `kube_resource_name` - name of resource being managed
* `kube_resource_configmaps` - a dict of ConfigMaps, mapping a reference name to a ConfigMap definition
* `kube_resource_manifest_files` - a list of resource definition template file names
* `kube_resource_secrets` - a dict of Secrets, mapping a reference name to a Secret definition
* `kube_resource_secrets_files` - a list of Secret definition template file names
* `kube_resource_validate` - configuration for the `validation` argument of the `k8s` module. e.g.
  ```
  kube_resource_validate:
    fail_on_error: true
    strict: true
  ```
* `kube_resource_wait` - whether to wait for resources to update (default `false`)
* `kube_resource_wait_timeout` - how long to wait in seconds for resources to update (ignored if kube_resource_wait is unset). Defaults to 120
* `kube_resource_unsafe_show_logs` - whether to show the logs when working with secrets. Defaults to `false`.
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
* `kube_resource_lookup_plugin` - The lookup plugin to use when reading manifests. If you're reading pure
  kubernetes manifests, you can use `file` which helps if those manifests contain jinja. Defaults to
  `template`


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

Versions
--------

This module relies on functionality of Ansible that won't be released until Ansible 2.8 in mid 2019.
The functionality has been included in this role, but will need to be removed once 2.8 is released.
As such, the role will be available by Ansible version.

Versions will be tagged `v2.7-x` where `x` is the release number of the role for version 2.7, with
a parallel `v2.8-y` version for use with Ansible 2.8 (or ansible devel branch before then)

License
-------

This role contains modules and filters from the Ansible project and thus inherit Ansible's license

GPL 3

Author Information
------------------

Will Thames (@willthames)
