kube-resource
=============

Manages Kubernetes resources based on a set of manifest templates

Requirements
------------

* openshift 0.7.3 or 0.8.0 (to be released)
* kubernetes
* k8s `module_utils` and module from Ansible with append_hash functionality
  (to be released after openshift 0.7.3/0.8.0 is released)

Role Variables
--------------

* `kube_resource_configmaps` - a dict of ConfigMaps, mapping a reference name to a ConfigMap definition
* `kube_resource_manifest_files` - a list of resource definition template file names
* `kube_resource_secrets` - a dict of Secrets, mapping a reference name to a Secret definition
* `kube_resource_secrets_files` - a list of Secret definition template file names
* `kube_resource_UNSAFE_show_logs` - whether to show the logs when working with secrets. Defaults to `no`.
  For use when troubleshooting problems with secret definitions.

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

See a more thorough worked example of [templates](https://github.com/willthames/ansiblefest2018/tree/master/ansible/playbooks/templates/docker-debug-versioned/v2)
and associated [inventory](https://github.com/willthames/ansiblefest2018/blob/master/ansible/inventory/group_vars/docker-debug-versioned.yml)

License
-------

BSD

Author Information
------------------

Will Thames (@willthames)
