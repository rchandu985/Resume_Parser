from pypdf import PdfReader

class PdfFileTextExtratcor:

    def __init__(self) -> None:
        pass

    def PdfFile(file_path):
        reader = PdfReader(file_path)

        return reader
    def TotalPages(file_path):
        return PdfFileTextExtratcor.PdfFile(file_path)._get_num_pages()
    
    def GetPdfFileText(file_path):

        text=""
        
        PdfFile=PdfFileTextExtratcor.PdfFile(file_path)

        get_total_pages=PdfFileTextExtratcor.TotalPages(file_path)
        
        for page_no in range(int(get_total_pages)):



            page = PdfFile.pages[page_no]
            
            rsm_text=page.extract_text()
            rst:str=rsm_text.replace(":"," ").replace("","")

            text+="\n"+rst
        
        return text.lower()
