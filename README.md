kube-resource
=============

Manages Kubernetes resources based on a set of manifest templates

Requirements
------------

* openshift
* kubernetes
* kubernetes-validate (optional)
* latest k8s `module_utils` and module from Ansible


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

License
-------

BSD

Author Information
------------------

Will Thames (@willthames)
