function confirmAction(action) {
    $('#confirmationModal').modal('show');
    $('#confirmationModal').find('.modal-body').text('Are you sure you want to ' + action + '?');

    return false;
}

function performAction() {
    $('#confirmationModal').modal('hide');
    // window.location.href = "/hr_employees/detail/{{employee.id}}/?message=success";
    return true;
}
