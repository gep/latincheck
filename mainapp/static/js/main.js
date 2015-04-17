/**
 * Created by gep on 4/17/15.
 */

$(function(){
    $('#main-form').submit(function(){
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            success: function(data){
                var modalWindow = $('#playinfo');
                modalWindow.find('div.modal-body').html(data);
                modalWindow.modal('show');
            }
        });

        console.log('sdasdasd');
        return false;
    });

});


