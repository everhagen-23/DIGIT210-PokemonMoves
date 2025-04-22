<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xpath-default-namespace="http://www.w3.org/1999/xhtml"
    version="3.0">
    
    <xsl:output method="text" indent="yes"/>
    <xsl:template match="tr">
        <xsl:apply-templates/>
    </xsl:template>


</xsl:stylesheet>