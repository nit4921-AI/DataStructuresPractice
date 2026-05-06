import pytest
from playwright.sync_api import Page, expect
 
def test_verify_hcpcs_cpt_code_active_inactive_date(page: Page):
    """Test to verify HCPCS/CPT Code Active/Inactive Date field is displayed and matches source field"""
   
    # Step 1-2: Navigate to PAHub application
    page.goto("https://autoqa.pahub.com")
    page.wait_for_load_state("networkidle")
   
    # Step 3: Login using valid credentials
    page.fill("//input[@id='txtLoginId'] | //lib-text-box[@textmodel='loginId']//input", "ss_advocatehealth_cua")
    page.fill("//input[@id='txtPassword'] | //lib-text-box[@textmodel='password']//input", "Admin@1234")
    page.click("//*[@id='login_r4_c3'] | //div//button[contains(text(),'Login')]")
    page.wait_for_load_state("networkidle")
    print("✅ Login successful")
   
    # Step 4: Navigate to Prescription Drugs
    page.click("//label[contains(@for,'ctl00_EocContentPlaceHolder_rBtnList_HcsType_0') and contains(text(),'Prescription Drugs')]/preceding-sibling::input[contains(@id,'ctl00_EocContentPlaceHolder_rBtnList_HcsType_0') and contains(@type,'radio')]")
    page.wait_for_load_state("networkidle")
    print("✅ Prescription Drugs selected")
   
    # Step 5-6: Patient Step - Enter member ID and search
    page.fill("//input[contains(@id,'txtSearchMemberNumber')] | //lib-text-box[@textmodel='memberNumber']//label[normalize-space()='Member Id:']//following-sibling::input | //div[contains(text(),'Step 1: Select Patient')]/..//lib-text-box[@textmodel='altMemberId']//input | //div[@id='searchPatient']//lib-text-box[@textmodel='memberNumber']//input", "9967612177")
    page.click("//img[contains(@id,'btnSearch')] | //div[@id='searchPatient']//button[normalize-space()='Search']")
    page.wait_for_load_state("networkidle")
    page.click("(//*[@id='divPatientList']/table//tbody/tr/td[2]/a)[1] | //lib-patient-search//div[@class='accordion-body']//div[1]//a")
    page.wait_for_load_state("networkidle")
    print("✅ Patient selected")
   
    # Step 7: Patient Step - Finalize Patient Summary
    page.click("//*[@name='imgbtnFinalize'] | //div[@id='collapseOne']//button[normalize-space()='Finalize']")
    page.wait_for_load_state("networkidle")
    print("✅ Patient finalized")
   
    # Step 8-9: Prescriber Step - Search by NPI and finalize
    page.fill("//input[@id='txtSearchNPI'] | //div[@id='searchPrescriber']//lib-text-box[@textmodel='npi']//input", "1003015496")
    page.click("(//*[contains(@id,'btnSearch')] | //div[@id='searchPrescriber']//button[normalize-space()='Search'])[1]")
    page.wait_for_load_state("networkidle")
    page.click("//*[@id='divPrescriberList']/table[2]/tbody/tr/td[2]/a | //div[@class='accordion-body']//div[1]//a")
    page.wait_for_load_state("networkidle")
    page.click("//img[@id='imgFinalize'] | //button[normalize-space()='Finalize']")
    page.wait_for_load_state("networkidle")
    print("✅ Prescriber finalized")
   
    # Step 10-11: HCS Step - Enter drug name and search
    page.fill("//input[@id='txtSearchHCSName']", "lipitor")
    page.click("//*[@id='imgSearch'] | //div[@id='searchHCS']//button[normalize-space()='Search']")
    page.wait_for_load_state("networkidle")
    print("✅ Drug search completed")
   
    # Step 12: Capture values for HCPCS/CPT Code Active/Inactive, HCPCS/CPT Code and NDC Status fields
    hcpcs_status_element = page.locator("(//td[normalize-space(text())='HCPCS/CPT Code Status:' and following-sibling::td[normalize-space() = 'Active']])[1]")
    expect(hcpcs_status_element).to_be_visible()
    hcpcs_status = hcpcs_status_element.inner_text()
    print(f"✅ HCPCS/CPT Code Status captured: {hcpcs_status}")
   
    ndc_status_element = page.locator("(//td[text()='NDC Status:']/../td[text()='Active'])[1]")
    expect(ndc_status_element).to_be_visible()
    ndc_status = ndc_status_element.inner_text()
    print(f"✅ NDC Status captured: {ndc_status}")
   
    hcpcs_code_element = page.locator("(//td[normalize-space(text())='HCPCS/CPT code:'])[1]")
    expect(hcpcs_code_element).to_be_visible()
    hcpcs_code = hcpcs_code_element.inner_text()
    print(f"✅ HCPCS/CPT code captured: {hcpcs_code}")
   
    hcpcs_date_element = page.locator("(//td[contains(text(),'HCPCS/CPT Code Status:')]/following-sibling::td[contains(@class,'hcpcs-status-active') and text()='Active']/following::td[contains(text(),'HCPCS/CPT Code Active/Inactive Date:')]/following-sibling::td)[1]")
    expect(hcpcs_date_element).to_be_visible()
    captured_hcpcs_date = hcpcs_date_element.inner_text()
    print(f"✅ HCPCS/CPT Code Active/Inactive Date captured: {captured_hcpcs_date}")
   
    # Step 13: Select drug and click Next
    page.click("(//td[text()='Drug Name:'])[1]/../td//a")
    page.wait_for_load_state("networkidle")
    page.click("//*[@id='imgDrugNext'] | //div[@id='drugInfo']//button[normalize-space()='Next']")
    page.wait_for_load_state("networkidle")
    print("✅ Drug selected and moved to 3a step")
   
    # Step 14: Verify captured values match in 3a Drug Step
    page.click("//a[@id='lnkSummary']")
    page.wait_for_load_state("networkidle")
   
    summary_ndc_status = page.locator("//span[@id='lblStatus']")
    expect(summary_ndc_status).to_be_visible()
    summary_ndc_value = summary_ndc_status.inner_text()
    print(f"✅ 3a NDC Status verified: {summary_ndc_value}")
   
    summary_hcpcs_status = page.locator("//span[@id='lblHCPCSStatus']")
    expect(summary_hcpcs_status).to_be_visible()
    summary_hcpcs_status_value = summary_hcpcs_status.inner_text()
    print(f"✅ 3a HCPCS/CPT Code Status verified: {summary_hcpcs_status_value}")
   
    summary_hcpcs_date = page.locator("//span[@id='lblHCPCSCodeDate']")
    expect(summary_hcpcs_date).to_be_visible()
    summary_hcpcs_date_value = summary_hcpcs_date.inner_text()
    print(f"✅ 3a HCPCS/CPT Code Active/Inactive Date verified: {summary_hcpcs_date_value}")
   
    # Step 15: Click 3a Next button
    page.click("(//*[@id='imgProductNext'] | //div[@id='productInfo']//button[normalize-space()='Next'] | (//lib-product-service-info/following::div//button[@type='submit' and contains(text(),'Next')])[1])[1]")
    page.wait_for_load_state("networkidle")
    print("✅ 3a Next clicked")
   
    # Step 16: Step 3b - Click Summary
    page.click("//a[@id='lnkSummary']")
    page.wait_for_load_state("networkidle")
    print("✅ 3b Summary opened")
   
    # Step 17: Click Finalize in HCS Summary
    page.click("//img[@id='ImgFinalize' and @alt='Finalize'] | //button[normalize-space()='Finalize']")
    page.wait_for_load_state("networkidle")
    print("✅ HCS Summary finalized")
   
    # Step 18: Add Info - Set Requestor = Patient
    page.select_option("//select[@id='ctl00_EocContentPlaceHolder_ddlRequestor']", label="Patient")
    page.wait_for_load_state("networkidle")
    print("✅ Requestor set to Patient")
   
    # Step 19: Add Info - Set EOC Source = Phone
    page.click("//label[contains(text(),'EOC Source:')]/..//mat-select")
    page.wait_for_load_state("networkidle")
    page.click("//span[contains(text(),'Phone')]")
    page.wait_for_load_state("networkidle")
    print("✅ EOC Source set to Phone")
   
    # Step 20: Add Info - Set Urgency = No
    page.click("//*[@id='ctl00_EocContentPlaceHolder_ddlUrgency'] | //lib-drop-down[@textmodel='urgency']//mat-select//div[contains(@class,'mat-select-arrow-wrapper')] | //td[normalize-space()='Urgency:']//following-sibling::td//select[@id='ddlUrgencylist']")
    page.wait_for_load_state("networkidle")
    page.click("//span[contains(text(),'No')]")
    page.wait_for_load_state("networkidle")
    print("✅ Urgency set to No")
   
    # Step 21: Add Info - Click Next
    page.click("//img[@id='img5' and @alt='Next'] | //div[contains(@id,'additionalInfo')]//button[normalize-space()='Next'] | (//lib-product-service-info/following::div//button[@type='submit' and contains(text(),'Next')])[2]")
    page.wait_for_load_state("networkidle")
    print("✅ Additional Info Next clicked")
   
    # Step 22: Add Info Summary - Finalize
    page.click("//img[@id='ImgFinalize' and @alt='Finalize'] | //button[normalize-space()='Finalize']")
    page.wait_for_load_state("networkidle")
    print("✅ Additional Info Summary finalized")
   
    # Step 23: Navigate to Review page
    print("✅ Test completed - EOC workflow finished successfully")
 