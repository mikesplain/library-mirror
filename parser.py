#!/usr/bin/env python

import yaml

# Outputs repos yaml in format for s6on/mirror-docker-tags-action requires

with open("repos.yaml", "r") as stream:
    try:
        y = yaml.safe_load(stream)
        s = ""

        firstKey = True
        for key in y:
            if firstKey:
                firstKey = False
                s = s + key + "["
            else:
                s = s + "," + key + "["
            firstValue = True
            for value in y[key]:
                if firstValue:
                    firstValue = False
                    s = s + str(value)
                else:
                    s = s + "," + str(value)
            s = s + "]"
        print(s)
    except yaml.YAMLError as exc:
        print(exc)