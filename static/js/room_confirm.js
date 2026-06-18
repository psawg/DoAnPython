(function () {
    var MESSAGES = {
        delete: function (room) {
            return (
                'Bạn có chắc chắn muốn xóa phòng "' +
                (room || '') +
                '"?\nHành động này không thể hoàn tác.'
            );
        },
        update: 'Bạn có chắc chắn muốn cập nhật thông tin phòng này?',
    };

    function bindDeleteLinks() {
        document.querySelectorAll('a.js-room-delete').forEach(function (link) {
            if (link.dataset.confirmBound === '1') {
                return;
            }
            link.dataset.confirmBound = '1';
            link.addEventListener('click', function (event) {
                var room = link.getAttribute('data-room-number') || 'này';
                if (!window.confirm(MESSAGES.delete(room))) {
                    event.preventDefault();
                }
            });
        });
    }

    function bindSubmitForms() {
        document.querySelectorAll('form.js-room-form-submit').forEach(function (form) {
            if (form.dataset.confirmBound === '1') {
                return;
            }
            form.dataset.confirmBound = '1';
            form.addEventListener('submit', function (event) {
                var action = form.getAttribute('data-confirm-action') || 'update';
                var message = MESSAGES[action] || MESSAGES.update;
                if (typeof message === 'function') {
                    message = message();
                }
                if (!window.confirm(message)) {
                    event.preventDefault();
                }
            });
        });
    }

    function bindEmployeeDeleteLinks() {
        document.querySelectorAll('a.js-employee-delete').forEach(function (link) {
            if (link.dataset.confirmBound === '1') {
                return;
            }
            link.dataset.confirmBound = '1';
            link.addEventListener('click', function (event) {
                var name = link.getAttribute('data-employee-name') || 'này';
                var message =
                    'Bạn có chắc chắn muốn xóa nhân viên "' +
                    name +
                    '"?\nHành động này không thể hoàn tác.';
                if (!window.confirm(message)) {
                    event.preventDefault();
                }
            });
        });
    }

    function bindSalaryDeleteLinks() {
        document.querySelectorAll('a.js-salary-delete').forEach(function (link) {
            if (link.dataset.confirmBound === '1') {
                return;
            }
            link.dataset.confirmBound = '1';
            link.addEventListener('click', function (event) {
                var name = link.getAttribute('data-employee-name') || 'này';
                var message =
                    'Bạn có chắc chắn muốn xóa bản ghi lương của "' +
                    name +
                    '"?\nHành động này không thể hoàn tác.';
                if (!window.confirm(message)) {
                    event.preventDefault();
                }
            });
        });
    }

    function init() {
        bindDeleteLinks();
        bindEmployeeDeleteLinks();
        bindSalaryDeleteLinks();
        bindSubmitForms();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
