(function () {
    'use strict';

    $('.todo-item').click(function () {
        var thisElement = $(this);
        var todoId = thisElement.attr('id');
        console.log(todoId);

        var request = $.ajax({
            url: "http://127.0.0.1:8000/check-todo/",
            method: "POST",
            data: {
                id: todoId
            }
        });

        request.done(function () {
            alert("SUCCESS!");
            if (thisElement.attr('checked')) {
                thisElement.attr("checked", null);
                thisElement.next().css("text-decoration", "none");
            } else {
                thisElement.attr("checked", "checked");
                thisElement.next().css("text-decoration", "line-through");
            }
        });

        request.fail(function () {
            alert("FAILLLL!");
        });
    });
})();