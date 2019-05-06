#!/usr/bin/env bash
{ set +x; } 2>/dev/null

( set -x; volume 0 ) && ( set -x; volume )
