
$(document).ready(function(){
    load_data();
    function load_data(query='')
    {
        $.ajax({
            url:"/sturecords",
            method:"POST",
            data:{query:query},
            success:function(data)
            { 
                $('tbody').html(data);
                $('tbody').append(data.htmlresponse);
            }
        })
    }
 
    $('#search_filter1').change(function(){
        $('#hidden_value1').val($('#search_filter1').val());
        var query = $('#hidden_value1').val(); 
        load_data(query);
    });
     
});
