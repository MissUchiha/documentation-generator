#!/usr/bin/env python

# Python 2/3 compatibility (NB: we require at least 2.7)

import os
import sys
import json
import logging
import yaml
import argparse
from git import Repo

def setup_logging():
    FORMAT = '%(asctime)s %(levelname)s %(message)s'
    logging.basicConfig(format=FORMAT, datefmt='%H:%M:%S', level=logging.DEBUG)

setup_logging()

# Parse the command line arguments we've been given
parser = argparse.ArgumentParser(description='Utility to sync source code of repoes for which docs should be generated.')

parser.add_argument('--projects-definition', type=str, required=True,
        help='Location of projects-definition.yaml file.')
parser.add_argument('--sourcesdir', type=str, required=True,
        help='Directory that contains or will contain directories of project sources.')

args = parser.parse_args()

def clone_repo(repo, sourcesdir):
    # clone repo or pull if repo already exists
    if not os.path.isdir(os.path.join(sourcesdir, repo['name'])):
        logging.info('Cloning repo {}'.format(repo['name']))
        cloned_repo = Repo.clone_from(repo['repoUrl'], os.path.join(sourcesdir, repo['name']))
    else:
        gitrepo = Repo.init(os.path.join(sourcesdir, repo['name']))
        gitrepo.remotes.origin.fetch()
        gitrepo.remotes.origin.pull()

# Grab a list of project definitions
with open(args.projects_definition, 'r') as data_file:
    # Parse the YAML file
    projects_definition = yaml.load(data_file)

# If product dooesn't have groups
if 'groups' not in projects_definition:
    if not os.path.isdir(args.sourcesdir):
        os.mkdir(args.sourcesdir)
    clone_repo(projects_definition['item'], args.sourcesdir)
else:
    # If product has groups, clone repo for every product in group
    for group in projects_definition['groups']:
        group_path = os.path.join(args.sourcesdir, group['name'].lower())
        # create parent folder
        if not os.path.isdir(args.sourcesdir):
            os.mkdir(args.sourcesdir)
        # create child folder
        if not os.path.isdir(group_path):
            os.mkdir(group_path)
        # search for subroups and iterate over them
        if 'subgroups' in group:
            for subgroup in group['subgroups']:
                for repo in subgroup['items']:
                    clone_repo(repo, group_path)
        # search for items and iterate over them
        elif 'items' in group:
            for repo in group['items']:
                    clone_repo(repo, group_path)
        else:
            clone_repo(group)
