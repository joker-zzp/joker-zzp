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

;;;;;;;;;;;;;;;;;;;;;;;;; elpy plug-in ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(require 'package)
(add-to-list 'package-archives
             '("elpy" . "https://jorgenschaefer.github.io/packages/"))

(package-initialize)

(defvar myElpy
  '(elpy))

(when (not package-archive-contents)
  (package-refresh-contents))


(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      myElpy)

(elpy-enable)

;;;;;;;;;;;;;;;;;;;;; end elpy ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; Download the theme plug-in ;;;;;;;;;;;;;;;;;;;;

(require 'package)

(add-to-list 'package-archives
       '("melpa" . "http://melpa.org/packages/") t)

(package-initialize)

(defvar myPackages
  '(better-defaults 
    auto-complete 
    py-autopep8 
    flycheck 
    material-theme))

(when (not package-archive-contents)
  (package-refresh-contents))

(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      myPackages)

(ac-config-default)

;;(setq elpy-rpc-python-command "python3")
;;(elpy-use-ipython)
(setq  python-shell-interpreter "ipython"
       python-shell-interpreter-args "-i --simple-prompt")

(load-theme 'material t) ;; load material theme

(global-set-key (kbd "RET") 'newline-and-indent)

(when (require 'flycheck nil t)
  (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
  (add-hook 'elpy-mode-hook 'flycheck-mode))

;; enable autopep8 formatting on save
(require 'py-autopep8)
(add-hook 'elpy-mode-hook 'py-autopep8-enable-on-save)
;;(add-to-list 'load-path (expand-file-name
;;                         "~/.emacs.d/el-get/python"))

;;;;;;;;;;;;;;;;;;;; end python plug-in ;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; system generation ;;;;;;;;;;;;;;;;;;;;

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

;;;;;;;;;;;;;;;;;;;; end system generation ;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; linux windows settings ;;;;;;;;;;;;;;;;;;;;
;; Start position
(set-frame-position (selected-frame) 75 60)

;; setting the height and width of the window
(set-frame-height (selected-frame) 70)
(set-frame-width (selected-frame) 130)

;; Setting English font
(set-face-attribute
  'default nil :font "DejaVu Sans Mono 11")
 
;; Setting Chinese Font
(dolist (charset '(kana han symbol cjk-misc bopomofo))
    (set-fontset-font (frame-parameter nil 'font)
                      charset
                      (font-spec :family "文泉驿等宽微米黑" :height 98)))

;;set transparent effect
(global-set-key [(f12)] 'loop-alpha)
(setq alpha-list '((100 100) (95 75) (90 70) (85 65) (80 60) (75 55) (65 45) (55 35)))
(defun loop-alpha ()
  (interactive)
  (let ((h (car alpha-list)))  ;; head value will set to
    ((lambda (a ab)
       (set-frame-parameter (selected-frame) 'alpha (list a ab))
       (add-to-list 'default-frame-alist (cons 'alpha (list a ab)))
       ) (car h) (car (cdr h)))
    (setq alpha-list (cdr (append alpha-list (list h))))
    )
)
;;;;;;;;;;;;;;;;;;;; end windows setting ;;;;;;;;;;;;;;;;;;;;
