#!/bin/bash

XCSP_3=$(cat)

echo "$XCSP_3" >> XCSP_3.xml
/concrete/bin/xcsp-3-concrete -a XCSP_3.xml
