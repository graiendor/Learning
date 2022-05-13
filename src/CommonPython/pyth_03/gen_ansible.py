from os import chdir, mkdir, path, getcwd
import yaml

if __name__ == '__main__':
    with open('todo.yml') as file:
        not_ansible = yaml.load(file, Loader=yaml.FullLoader)
        print(not_ansible)
    not_ansible.update('')
    with open('deploy.yml', 'w') as file:
        yaml.dump(not_ansible, file)
