
;;;;;;;;;;;;;;;;;;;; system generation ;;;;;;;;;;;;;;;;;;;;
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   (quote
    (ein py-autopep8 flycheck elpy color-theme-modern better-defaults))))
 
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
;;;;;;;;;;;;;;;;;;;; End syetem generation ;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; windows settings ;;;;;;;;;;;;;;;;;;;;
;; Start position
(set-frame-position (selected-frame) 40 80)

;; setting the height and width of the window
(set-frame-height (selected-frame) 50)
(set-frame-width (selected-frame) 150)

;; Setting English font
(set-face-attribute
  'default nil :font "Inconsolata 12")
 
;; Setting Chinese Font
(dolist (charset '(kana han symbol cjk-misc bopomofo))
    (set-fontset-font (frame-parameter nil 'font)
                      charset
                      (font-spec :family "华文楷体" :size 14)))

;;;;;;;;;;;;;;;;;;;; end windows setting ;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; Basic setup ;;;;;;;;;;;;;;;;;;;;
;; Cancel the start interface
(setq inhibit-startup-message t)

;; Clean interface
(tool-bar-mode 0)
(menu-bar-mode 0)
(scroll-bar-mode 0)

;;;;;;;;;;;;;;;;;;;; end Basic setup ;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; Personal settings ;;;;;;;;;;;;;;;;;;;;
;; No backup files are produced when saved
(setq make-backup-files nil)

;; Tab change space
(setq-default indent-tabs-mode nil)

;; when asking yes or no, answer with y-n
(fset 'yes-or-no-p 'y-or-n-p)

;; Automatic cursor for cursor
(mouse-avoidance-mode 'animate)

;; Extension matching
(show-paren-mode t)

;;Automatic completion symbol
(electric-pair-mode t)

;; Roll up and down
(setq scroll-conservatuvely 10000 scroll-margin 3 scroll-step 1)

;; Korea show here
;;(global-hl-line-mode t)

;; line number
(global-linum-mode t)
(setq linum-format "%d->")

;; time settings
(display-time-mode t)
(setq display-time-24hr-format t)
(setq display-time-day-and-date t)

;; show Column number
(column-number-mode t)

;; parenthesis matching
(show-paren-mode t)

;;;;;;;;;;;;;;;;;;;; End personal settings ;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; Download the theme plug-in ;;;;;;;;;;;;;;;;;;;;
(require 'package)

(add-to-list'package-archives
 '("melpa" . "http://melpa.org/packages/") t)

(package-initialize)

;;(defvar myThemePackages
;;  '(color-theme-modern))
;;
;;(when (not package-archive-contents)
;;  (package-refresh-contents))
;;
;;(mapc #'(lambda (package)
;;    (unless (package-installed-p package)
;;      (package-install package)))
;;      myThemePackages)

;;(require 'color-theme-modern)
;;(load-theme 'euphoria t t)
;;(enable-theme 'euphoria)

(defvar myPythonPackages
  '(better-defaults
    elpy
    ein
    flycheck
    material-theme
    py-autopep8))

(when (not package-archive-contents)
  (package-refresh-contents))


(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      myPythonPackages)

;;;;;;;;;;;;;;;;;;;; End dowload the theme plug-in ;;;;;;;;;;;;;;;;;;;;

(load-theme 'material t) ;; load material theme
;;(global-linum-mode t)

;;;;;;;;;;;;;;;;;;;; elpy ;;;;;;;;;;;;;;;;;;;;
(require 'elpy)
(elpy-enable)
(elpy-use-ipython)

;;;;;;;;;;;;;;;;;;; begin flycheck ;;;;;;;;;;;;;;;;;;;;;;;
(when (require 'flycheck nil t)
  (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
  (add-hook 'elpy-mode-hook 'flycheck-mode))

;;;;;;;;;;;;;;;;;;;; end flycheck ;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; py-autopep8 ;;;;;;;;;;;;;;;;;;;;

(require 'py-autopep8)
(add-hook 'elpy-mode-hook 'py-autopep8-enable-on-save)

;;;;;;;;;;;;;;;;;;;; end py-autopep8 ;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;; begin python ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;( require 'python )
;; use ipython 
(setq python-command "ipython") 
(setq 
      python-shell-interpreter "ipython" 
      python-shell-interpreter-args "" 
      python-shell-prompt-regexp "In \\[[0-9]+\\]: " 
      python-shell-prompt-output-regexp "Out\\[[0-9]+\\]: " 
      python-shell-completion-setup-code "from IPython.core.completerlib import module_completion" 
      python-shell-completion-string-code "';'.join(__IP.complete('''%s'''p))\n" 
      python-shell-completion-module-string-code "" ) 
( add-hook 'python-mode-hook
    ( lambda ()
        ( set-variable 'indent-tabs-mode nil )
      ( define-key python-mode-map ( kbd "RET" ) 'newline-and-indent ) ) )
;;;;;;;;;;;;;;;;;;;;;;;; end python ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; begin yasnippet ;;;;;;;;;;;;;;;;;;;;;
(add-to-list 'load-path "~/.emacs.d/plugins/yasnippet")
(require 'yasnippet)
(setq yas/prompt-functions 
   '(yas/dropdown-prompt yas/x-prompt yas/completing-prompt   
    yas/ido-prompt yas/no-prompt))
(yas/global-mode 1)
(yas/minor-mode-on)
;;;;;;;;;;;;;;;;;;;; end yasnippet ;;;;;;;;;;;;;;;;;;;;;
