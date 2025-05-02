<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:output method="text" indent="yes"/>
    
    <xsl:template match="moveSet">
        <xsl:for-each select="move">
            <!--<xsl:if test="type = 'status'">
                <xsl:value-of select="description"/>
                <xsl:text>
</xsl:text>
            </xsl:if>-->
            
            <!--<xsl:if test="type = 'physical'">
                <xsl:value-of select="description"/>
                <xsl:text>
</xsl:text>
            </xsl:if>-->
            
            <xsl:if test="type = 'special'">
                <xsl:value-of select="description"/>
                <xsl:text>
</xsl:text>
            </xsl:if>
            
        </xsl:for-each>
    </xsl:template>
    
</xsl:stylesheet>