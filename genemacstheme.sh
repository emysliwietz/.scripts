#!/bin/bash

colors=$(cat ~/.cache/wal/colors)

c0=$(echo $colors | field 1)
c1=$(echo $colors | field 2)
c2=$(echo $colors | field 3)
c3=$(echo $colors | field 4)
c4=$(echo $colors | field 5)
c5=$(echo $colors | field 6)
c6=$(echo $colors | field 7)
c7=$(echo $colors | field 8)
c8=$(echo $colors | field 9)
c9=$(echo $colors | field 10)
c10=$(echo $colors | field 11)
c11=$(echo $colors | field 12)
c12=$(echo $colors | field 13)
c13=$(echo $colors | field 14)
c14=$(echo $colors | field 15)
c15=$(echo $colors | field 16)

echo "(require 'base16-theme)

;; colours generated dynamically by wal
(defun set-wal-colors () (setq base16-wal-colors
			       '(:base00 \"$c0\"
					 :base01 \"$c1\"
					 :base02 \"$c2\"
					 :base03 \"$c3\"
					 :base04 \"$c4\"
					 :base05 \"$c5\"
					 :base06 \"$c6\"
					 :base07 \"$c7\"
					 :base08 \"$c8\"
					 :base09 \"$c9\"
					 :base0A \"$c10\"
					 :base0B \"$c11\"
					 :base0C \"$c12\"
					 :base0D \"$c13\"
					 :base0E \"$c14\"
					 :base0F \"$c15\")))

(defvar base16-wal-colors nil \"All colors for base16-wal are defined here.\")
(set-wal-colors)

;; Define the theme
(deftheme base16-wal)

;; Add all the faces to the theme
(base16-theme-define 'base16-wal base16-wal-colors)

;; Mark the theme as provided
(provide-theme 'base16-wal)

(provide 'base16-wal)"
