class Locus():

#Login
    btn_Login = "//button//div//p[contains(text(),'Login')]"
    btn_continue = "//button[@data-test-id = 'button-personnel-continue-to-login']"
    txt_user_id = "//input[@data-test-id='input-userId']"
    txt_password = "//input[@data-test-id = 'input-password']"
    alert_message = "//div[@data-test-id='error-auth0']"


#Dashboard
    left_side_bar = "//div[@class='LeftBar__dashboardWrap___1Ijsu']"
    title_user = "//div[@class='UserMenuItem__title___3q4j7']"
    icn_profile = "//div[@data-test-id = 'personnelMenu-accountIcon']"
    icn_search = "//div[@class='TableAddons__item___2od--']//button[@data-react-toolbox='button']"
    txt_search_area = "//input[@placeholder='Search Tasks by ID, address, name...']"
    search_result = "//div[@class='fixedDataTableRowLayout_rowWrapper']"

#Create Task
    btn_add_task = "//button[@testid='addVisit']"
    btn_proceed = "//button[@testid = 'proceedTaskCreation']"
    txt_task_id = "//input[@testid='enterVistId']"
    drp_team = "//div[@class='ListCard__cardTitle___jOgnk TeamRenderer__cardTitle___1P7-r']"
    drp_option = "//div[@data-test-id='select-selectMenu']"
    drp_type = "//div[@class='ListCard__left___2QOwU']"
    drp_type_option = "//div[@testid='option-2']"
    btn_slot = "//div[@class='SlotCard__slotCardTitle___3B_-B']"
    txt_slot = "//input[@placeholder='Enter SLA (min)']"
    task_modal = "//div[@class='OverlayDialog__dialog___18NSD TaskDetails__dialog___o3W5S']"
    btn_save = "//button[@testid='save']"
    btn_create_task = "//button[@testid='createTask']"
    txt_address = "react-select-5-input"
    use_address = "//div[@data-test-id='select-selectMenu']"
    task_header = "//div[@class='OverlayDialog__dialog___18NSD TaskDetails__dialog___o3W5S']//header"
    icn_close = "//button[@class='theme__toggle___3PAFQ theme__neutral___3Z1P6 theme__inverse___3uKC8']"


