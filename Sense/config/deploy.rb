# config valid only for current version of Capistrano
lock '3.4.0'

set :application, 'SenseWeb'
set :repo_url, 'https://github.com/mraaa711128/SenseWeb.git'

# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
set :deploy_to, '/srv/SenseWeb'

# Default value for :scm is :git
# set :scm, :git

# Default value for :format is :pretty
# set :format, :pretty

# Default value for :log_level is :debug
# set :log_level, :debug

# Default value for :pty is false
# set :pty, true

# Default value for :linked_files is []
set :linked_files, fetch(:linked_files, []).push('Sense/Sense/settings/__init__.py','Sense/Sense/settings/default.py','Sense/Sense/settings/production.py')

# Default value for linked_dirs is []
set :linked_dirs, fetch(:linked_dirs, []).push('Sense/Sense/settings')

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for keep_releases is 5
set :keep_releases, 20

namespace :deploy do

  after :restart, :clear_cache do
    on roles(:web), in: :groups, limit: 3, wait: 10 do
      # Here we can do anything such as:
      # within release_path do
      #   execute :rake, 'cache:clear'
      # end
    end
  end

end
